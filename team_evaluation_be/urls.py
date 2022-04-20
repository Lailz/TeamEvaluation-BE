
from django.contrib import admin
from django.urls import path
from team_app import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # users
    path("signup", views.SignupView.as_view(), name="signup"),
    path("signin", views.SigninView.as_view(), name="signin"),

    # semesters
    path("semesters/create", views.SemesterCreateView.as_view(),
         name="semesters-create"),
    path("semesters", views.SemesterListView.as_view(), name="semesters-list"),
]
