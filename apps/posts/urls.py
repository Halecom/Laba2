from django.urls import path

from apps.posts import views

urlpatterns = [
    path("", views.index),
    path("<int:post_id>/delete/", views.delete_post),
    path("<int:post_id>/edit/", views.update_post),
    path("<int:post_id>/<str:type>/", views.react),
]
