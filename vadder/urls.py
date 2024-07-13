from django.urls import path
import vadder.views.views as views
import vadder.views.users as users

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("getdata/", views.getdata, name="getdata"),
    path("login/", users.LoginUser.as_view(), name="login"),
    path("logout/", users.logout_user, name="logout"),

]
