from django.urls import path
from .views import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("getdata", views.getdata, name="getdata"),
]
