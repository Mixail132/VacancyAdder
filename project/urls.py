import vadder.views.users as usr
import vadder.views.views as act
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("vadder.urls")),
    path("admin/", admin.site.urls, name="admin"),
    path("login/", usr.LoginUser.as_view(), name="login"),
    path("logout/", usr.logout_user, name="logout"),
]
