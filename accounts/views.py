from django.shortcuts import render, redirect
from accounts.forms import LoginForm, SignupForm
from django. contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def login_(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if not user:
                form.add_error("username", "Invalid username or password")
            else:
                login(request, user)
                return redirect("list_projects")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout_(request):
    logout(request)
    return redirect("login")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            if password != password_confirmation:
                form.add_error("password", "Passwords do not match")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                login(request, user)
                return redirect("list_projects")
                user.save()
                login(request, user)
                return redirect("list_projects")
    else:
        form = SignupForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)