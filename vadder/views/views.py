from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError


def home(request):
    """ Shows tha add vacancy form."""
    if request.user.is_authenticated:
        return render(request, "add.html")
    return render(request, "login.html")


def getdata(request):
    """ Gets the vacancy text. """
    levels = []
    for level in ["junior", "senior", "middle"]:
        try:
            levels.append(request.POST[level])
        except MultiValueDictKeyError:
            continue
    jobtypes = []
    for jobtype in ["office", "remote", "flexible", "fulltime"]:
        try:
            jobtypes.append(request.POST[jobtype])
        except MultiValueDictKeyError:
            continue
    try:
        english = request.POST["english"]
    except MultiValueDictKeyError:
        english = ""

    vacancy_data = {
        "body": request.POST["body"],
        "vacancy": request.POST["vacancy"],
        "profession": request.POST["profession"],
        "city": request.POST["city"],
        "experience": request.POST["experience"],
        "company": request.POST["company"],
        "contacts": request.POST["contacts"],
        "english": english,
        "jobtypes": jobtypes,
        "levels": levels,
    }

    for k, v in vacancy_data.items():
        print(k, ":", v)

    return HttpResponseRedirect(reverse("home"))


