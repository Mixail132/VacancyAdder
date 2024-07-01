from django.shortcuts import render


def home(request):
    """ Shows the home page."""
    return render(request, "main/home.html")
