from django.db import models
from django.contrib.auth.models import User


HIDE = (
    ("not_hidden", "Show on Dashboard"),
    ("hidden",  "Hide from Dashboard")
)
COLORS = (
    ("#FF0000", "Red"),
    ("#FF7F00", "Orange"),
    ("#FFFF00", "Yellow"),
    ("#00FF00", "Green"),
    ("#00FFFF", "Cyan"),
    ("#0000FF", "Blue"),
    ("#7F00FF", "Violet"),
    ("#FF00FF", "Magenta"),
)


class Project(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(choices=COLORS)

    def __str__(self):
        return self.name


class WorkState(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()
    is_hidden = models.CharField(choices=HIDE)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Comment(models.Model):
    body = models.CharField(max_length=500)
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    parent_post = models.ForeignKey('TaskPost', on_delete=models.PROTECT)


class TaskPost(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    work_state = models.ForeignKey(WorkState, on_delete=models.PROTECT, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    due_date = models.DateField()
    body = models.TextField(max_length=1000)
    show_on_calendar = models.BooleanField(null=True, blank=True)
    type = models.TextField(max_length=50, null=True, blank=True)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    comments = models.ForeignKey(Comment,on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title



