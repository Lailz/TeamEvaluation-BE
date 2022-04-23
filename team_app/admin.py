from django.contrib import admin

from team_app.models import Project, Semester, Team

admin.site.register(Semester)
admin.site.register(Project)
admin.site.register(Team)
