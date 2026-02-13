from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user) # auto-login after registration
            return redirect("login")
        
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