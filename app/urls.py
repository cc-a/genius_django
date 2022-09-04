from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("info", views.info, name="info"),
    path("access", views.access, name="access"),
    path("stats", views.stats, name="stats"),
]
