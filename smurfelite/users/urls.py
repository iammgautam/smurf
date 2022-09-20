from django.urls import path

from . import views
app_name = 'user'

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path('logout/', views.logout_user, name='logout'),
    path("register/", views.user_register, name="register"),
    path("profile/", views.profile, name="profile"),
]
