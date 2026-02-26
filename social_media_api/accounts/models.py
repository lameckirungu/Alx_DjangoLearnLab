from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models import F, Q

class User(AbstractUser):
    
    bio = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name="followers", blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=32, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Profile({self.user.username})"
    
class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following_relationships")
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follower_relationships")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["follower", "following"],
                name="unique_follower_following",
            ),
            models.CheckConstraint(
                check=~Q(follower=F("following")),
                name="prevent_self_follow",
            ),
        ]
    
    def __str__(self):
        return f"{self.follower} -> {self.following}"