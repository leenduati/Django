# Created this urls.py in app

from django.urls import include, path
from first_app import views

urlpatterns = [
    path("", views.index, name="index"),
]
