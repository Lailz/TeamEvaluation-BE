
from django.contrib import admin
from django.urls import path
from team_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup", views.SignupView.as_view(), name="signup"),
    path("signin", views.SigninView.as_view(), name="signin")
]
