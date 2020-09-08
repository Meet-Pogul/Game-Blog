from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    context = {  # context is a set of variables
        'variable': 'Hello World'
    }
    return render(request, 'index.html', context)  # context pass variable


def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'about.html')


def blog(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'blog.html')


def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        con = Contact(name=fname + " " + lname, email=email, desc=desc, date=datetime.today())
        con.save()
        messages.success(request, 'Thank You for contacting us, We will contact you as soon as possible')
    return render(request, 'contact.html')


def blog1(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "detailblog1.html")
