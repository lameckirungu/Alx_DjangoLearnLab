from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Comme-separated tags, e.g django, python, web"
    )
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["tags"].initial = ", ".join(
                self.instance.tags.values_list("name", flat=True)
            )

    def save(self, commit=True):
        post = super().save(commit=commit)
        if commit:
            raw = self.cleaned_data.get("tags", "")
            names = [t.strip().lower() for t in raw.split(",") if t.strip()]
            tag_objs = []
            for name in set(names):
                tag, _ = Tag.objects.get_or_create(name=name)
                tag_objs.append(tag)
            post.tags.set(tag_objs)
        return post

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ["content"]
