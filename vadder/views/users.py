from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from vadder.forms import LoginUserForm
from django.template import loader
from django.http import HttpResponse


def logout_user(request):
    logout(request)
    return redirect("login")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"
    def get_success_url(self):
        return reverse_lazy("home")


def if_authenticated(allowed_action):
    def action(request):
        if not request.user.is_authenticated:
            context = {}
            template = loader.get_template("noname.html")
            return HttpResponse(template.render(context, request))
        return allowed_action(request)
    return action
