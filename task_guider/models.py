from django.db import models

class TodoPost(models.Model):
    title = models.CharField(max_length=100)