
from django.contrib import admin
from django.urls import path
from team_app import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # users
    path("signup", views.SignupView.as_view(), name="signup"),
    path("signin", views.SigninView.as_view(), name="signin"),

    # semesters
    path("semesters", views.SemesterListCreateView.as_view(), name="semesters"),

    # projects
    path("semesters/<int:semester_id>/projects/",
         views.ProjectCreateView.as_view(), name="projects-create"),

    # teams
    path("projects/<int:project_id>/teams/",
         views.TeamCreateView.as_view(), name="teams-create"),

    # criteria
    path("criterias", views.CriteriaListCreateView.as_view(), name="criterias"),
]
