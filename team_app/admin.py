from django.contrib import admin

from team_app.models import Criteria, Project, Report, Semester, Team

admin.site.register(Semester)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Criteria)
admin.site.register(Report)
