from django.shortcuts import render
from django.views import generic
from .models import Project, TodoPost, WorkState

class Dashboard(generic.ListView):
    queryset = TodoPost
    template_name = "dashboard.html"
    def get_context_data(self):
        context = {
            'TodoPost': 'test',
            'name':'Rob'
        }
        return context

class DashboardDetail(generic.DetailView):
    pass