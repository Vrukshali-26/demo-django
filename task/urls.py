from django.urls import path
from . import views

urlpatterns = [
    path("", views.task, name="tasks"),
    path("add/", views.add, name="add")
]

