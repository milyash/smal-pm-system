from operator import attrgetter

from django.http import HttpResponse
from django.shortcuts import render

from .models import Project, ProjectMilestone, Milestone


def index(request):
    if request.method == 'GET':

        milestones = Milestone.objects.all()
        projects = {project: dict.fromkeys(list(map(attrgetter('id'), milestones)), None)
                    for project in Project.objects.all()}

        for project_milestone in ProjectMilestone.objects.all():
            projects[project_milestone.project][project_milestone.milestone.id] = project_milestone.completion_date

        context = {'projects': projects, 'milestones': milestones}
        return render(request, 'project/index.html', context)
    return HttpResponse('POST requests are not available on this page.')
