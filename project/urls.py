from django.urls import path, include


urlpatterns = [
    path("vadder/", include("vadder.urls")),
]
