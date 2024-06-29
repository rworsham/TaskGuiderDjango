from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    color = models.IntegerField()
    posts = models.ManyToManyField('TodoPost')

class Comment(models.Model):
    body = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    parent_post = models.ForeignKey('TodoPost', on_delete=models.PROTECT)



class TodoPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100)
    work_state = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    body = models.TextField(max_length=1000)
    type = models.TextField(max_length=50)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    comments = models.ForeignKey
