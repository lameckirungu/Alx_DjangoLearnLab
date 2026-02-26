from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("posts/feed/", FeedView.as_view(), name="feed"),
    path("posts/<int:pk>/like/", LikePostView.as_view(), name="likes"),
    path("posts/<int:pk>/unlike/", UnlikePostView.as_view(), name="unlikes"),
]

urlpatterns += router.urls