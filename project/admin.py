from django.contrib import admin

from .models import Manager, Project, Milestone, ProjectMilestone

admin.site.register(Manager)
admin.site.register(Project)
admin.site.register(Milestone)
admin.site.register(ProjectMilestone)
