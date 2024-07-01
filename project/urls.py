import vadder.views.users as usr
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("vadder.urls")),
    path("admin/", admin.site.urls),
    path("login/", usr.LoginUser.as_view(), name="login"),
    path("logout/", usr.logout_user, name="logout"),
]
