from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register, profile, SearchResultsView, PostByTagListView
from .views import (
    PostListView, PostUpdateView, 
    PostCreateView, PostDeleteView, PostDetailView,

    CommentListView, CommentUpdateView, 
    CommentCreateView, CommentDeleteView, CommentDetailView

    
)

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),

    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    path("comment/", CommentListView.as_view(), name="comment-list"),
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

    path("search/", SearchResultsView.as_view(), name="search-results"),
    path("tags/<str:tag_name>/", PostByTagListView.as_view(), name="posts-by-tag"),
]   