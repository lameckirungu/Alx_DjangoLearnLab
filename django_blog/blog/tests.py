from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentPermissionTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="author", password="password12345")
        self.other= User.objects.create_user(username="other", password="password12345")
        self.comment = Comment.objects.create(author=self.author, content="This is a comment")


