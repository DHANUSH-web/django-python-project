from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.home, name="Blogs | Home"),
    path(route="about/", view=views.about, name="Blogs | About"),
]