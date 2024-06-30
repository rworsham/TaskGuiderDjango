from django.shortcuts import render
from django.views import generic
from .models import Project, TodoPost, WorkState

class Dashboard(generic.ListView):
    queryset = TodoPost.objects
    template_name = "dashboard.html"


class DashboardDetail(generic.DetailView):
    pass