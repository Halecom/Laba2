from django.urls import path

from apps.users import views

urlpatterns = [
    path("registration/", views.register),
    path("authorization/", views.authorization),
    path("logout/", views.logout),
]
