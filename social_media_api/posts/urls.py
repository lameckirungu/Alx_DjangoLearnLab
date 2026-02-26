from .views import PostViewSet, CommentViewSet, FeedView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("feed/", FeedView.as_view(), name="feed"),
]

urlpatterns += router.urls