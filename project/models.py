from django.contrib.auth.models import AbstractUser
from django.db import models


class Manager(AbstractUser):
    name = models.CharField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = 'Manager'

    def __str__(self):
        return f'{self.name}'


class Milestone(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Milestone name')
    order = models.IntegerField(unique=True, verbose_name='Order of the milestone',
                                help_text='Use this field to define the order of milestones')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Project name')
    owner = models.ForeignKey(Manager, null=True, on_delete=models.SET_NULL)
    milestones = models.ManyToManyField(Milestone, related_name='projects', through='ProjectMilestone')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'"{self.name}" managed by {self.owner}'


class ProjectMilestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    completion_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Project-Milestone mapping'
        db_table = 'projects_milestones'

    def __str__(self):
        return f"Milestone {self.milestone} of project {self.project} is due on {self.completion_date or '-'}"
