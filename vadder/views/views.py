from django.shortcuts import render


def home(request):
    """ Shows tha add vacancy form."""
    if request.user.is_authenticated:
        return render(request, "add.html")
    return render(request, "login.html")
