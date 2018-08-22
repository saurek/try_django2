from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 666,
        "my_list": [1615, 156 ,998, "fff000"]
    }
    return render(request, "about.html", my_context)


def social_view(*args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")
