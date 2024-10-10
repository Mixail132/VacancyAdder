from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("vadder/", include("vadder.urls")),
    path("admin/", admin.site.urls)
]
