from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return render(request, 'login.html')


def sign(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=username, password=password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        login(request, user)
        return redirect("/")
    return render(request, 'sign.html')
