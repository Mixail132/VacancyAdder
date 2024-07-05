from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from datetime import datetime
from .bases import DataBaseHandler
from .clears import prepare_vacancy_items


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
    levels = ", ".join(levels)

    jobtypes = []
    for jobtype in ["office", "remote", "flexible", "fulltime"]:
        try:
            jobtypes.append(request.POST[jobtype])
        except MultiValueDictKeyError:
            continue
    jobtypes = ", ".join(jobtypes)

    try:
        english = request.POST["english"]
    except MultiValueDictKeyError:
        english = ""

    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    vacancy_data = {
        "body": request.POST["body"],
        "vacancy": request.POST["vacancy"],
        "title": request.POST["vacancy"],
        "profession": request.POST["profession"],
        "city": request.POST["city"],
        "experience": request.POST["experience"],
        "company": request.POST["company"],
        "contacts": request.POST["contacts"],
        "chat_name": request.POST["contacts"],
        "vacancy_url": request.POST["contacts"],
        "salary": request.POST["salary"],
        "english": english,
        "job_type": jobtypes,
        "level": levels,
        "created_at": today,
        "time_of_public": today,
    }
    if "junior" in levels:
        vacancy_data["profession"] = f'junior, {vacancy_data["profession"]}'

    vacancy_keys, vacancy_values = prepare_vacancy_items(vacancy_data)

    database_handler = DataBaseHandler()
    database_handler.insert_vacancy(vacancy_keys, vacancy_values)

    return HttpResponseRedirect(reverse("home"))
