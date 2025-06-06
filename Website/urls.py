from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("tours", views.tours, name="tours"),
               path("register", views.register, name="register"),
               path("login", views.login, name="login"),
               path("about", views.about, name="about")
               ]