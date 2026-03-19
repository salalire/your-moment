from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse




def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")
def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")

def home(request):
    return render(request, "home.html")


@login_required
def profile(request):
    return render(request, "accounts/profile.html")




@login_required
def profile(request):
    if request.method == "POST":
        image = request.FILES.get("profile_picture")

        if image:
            request.user.profile_picture = image
            request.user.save()

            return JsonResponse({
                "image_url": request.user.profile_picture.url
            })

    return JsonResponse({"error": "Invalid request"})