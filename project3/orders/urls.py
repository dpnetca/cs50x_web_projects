from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("register_user", views.register_user, name="register_user"),
    path("user_detail", views.user_detail, name="user_detail"),
    path("update_user", views.update_user, name="update_user"),
]
