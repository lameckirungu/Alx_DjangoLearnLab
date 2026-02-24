from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    bio = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name="following", blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=32, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Profile({self.user.username})"