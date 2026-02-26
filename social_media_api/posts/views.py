from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS, IsAuthenticated

from .models import Post, Comment
from accounts.models import Follow
from .serializers import PostSerializer, CommentSerializer

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
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        followed_user_ids = Follow.objects.filter(author_id__in=followed_user_ids).select_related("author").order_by("-created_at")