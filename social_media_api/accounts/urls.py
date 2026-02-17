from .views import RegisterView, LoginView, ProfileView
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import User

from django.urls import path

urlpatterns = [
    path("api/register", RegisterView.as_view(), name="register"),
    path("api/login", LoginView.as_view(), name="login"),
    path("api/register", ProfileView.as_view(), name="profile"),
]