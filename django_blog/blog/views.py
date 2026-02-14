from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from .models import Post, Comment
from .forms import RegisterForm, PostForm, CommentForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user) # auto-login after registration
            return redirect("post-list")
        
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        request.user.email = email
        request.user.save()
        return redirect("profile")
    return render(request, "blog/profile.html")


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]

class PostByTagListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.tag_slug = self.kwargs["tag_slug"]
        return Post.objects.filter(tags__name=self.tag_slug).order_by("-published_date")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_tag"] = self.tag_slug
        return context
    
class SearchResultsView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q", "").strip()
        if not query:
            return Post.objects.none()
        return Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct().order_by("-published_date")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "").strip()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"    

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user


class CommentListView(ListView):
    model = Comment
    template_name = "blog/comment_list.html"
    context_object_name = "comments"
    ordering = ["-updated_at"]

class CommentDetailView(DetailView):
    model = Comment
    template_name = "blog/comment_detail.html"
    context_object_name = "comment"

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.post.pk})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def test_func(self) -> bool | None:
        comment = self.get_object()
        return comment.author == self.request.user
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_delete.html"
    success_url = reverse_lazy("comment-list")

    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user
