from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    color = models.IntegerField()
    posts = models.ManyToManyField('TodoPost')



class TodoPost(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    work_state = models.IntegerField()
    date_created = models.DateTimeField()
    due_date = models.DateTimeField()
    body = models.TextField(max_length=1000)
    type = models.TextField(max_length=50)
    project_id = models.ForeignKey(Project.id, on_delete=models.CASCADE)
    project = models.ForeignKey(Project.name, on_delete=models.CASCADE)
    author = models.OneToOneField(User.username, on_delete=models.CASCADE)
    comments = models.ForeignKey
