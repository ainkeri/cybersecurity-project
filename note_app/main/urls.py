from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notes/", views.notes, name="notes"),
    path("notes/<int:note_id>/", views.detail, name="detail"),
    path("notes/<int:note_id>/delete", views.delete, name="delete"),
    path("new_note/", views.new_note, name="new_note"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout")
]