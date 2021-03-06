from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return render(request, "accounts/logged.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "ns/login.html", context)
        login(request, user)
        return redirect('../admin')
    return render(request, "ns/login.html", {})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "ns/logout.html", {})

def register(request):
    return render(request, "accounts.register.html", {})
