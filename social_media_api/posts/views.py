from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, permissions, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from rest_framework.response import Response

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification

class isOwnerOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadonly]
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-created_at")
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by("-created_at")
    permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadonly]
    ordering_fields = ['updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")
    
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)

        like, created = Like.objects.get_or_create(
            user=request.user,
            post=post,
        )
        if not created:
            return Response(
                {"detail": "You already liked this post."},
                status=status.HTTP_200_OK,
            )

        # Notify post owner (skip self-like notification)
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
            )

        return Response(
            {"detail": "Post liked successfully."},
            status=status.HTTP_201_CREATED,
        )

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()

    def delete(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)

        deleted_count, _ = Like.objects.filter(
            user=request.user,
            post=post,
        ).delete()

        if deleted_count == 0:
            return Response(
                {"detail": "You have not liked this post."},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"detail": "Post unliked successfully."},
            status=status.HTTP_200_OK,
        )