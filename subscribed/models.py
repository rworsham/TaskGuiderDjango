from django.db import models
from django.contrib.auth.models import User
from task_guider.models import Project

class Subscribed(models.Model):
    email = models.ForeignKey(User, on_delete=models.PROTECT)
    subscribed_object = models.ForeignKey(Project, on_delete=models.CASCADE)

