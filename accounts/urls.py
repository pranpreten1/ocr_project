from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("login", views.users_login, name="login"),
    path("logout", views.users_logout, name="logout"),
    path("signup", views.users_signup, name="signup")
]
