from django.urls import path
from webapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("html/", views.html, name="html"),
    path("maplocal/", views.maplocal, name="maplocal"),
    path("mapoverview/", views.mapoverview, name="mapoverview"),
]