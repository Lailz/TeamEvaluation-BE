from django.contrib import admin

from team_app.models import Criteria, Project, Semester, Team

admin.site.register(Semester)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Criteria)
