from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.utils import timezone
from .models import Project, TodoPost, WorkState, TaskType, Comment
from .forms import TaskForm



def test(request):
    context = {'form': TaskForm()}
    # if form.is_valid():
    #     for x in form.cleaned_data:
    #         print(x)
    # else:
    #     return render(request, "task_guider/test.html")
    return render(request, "test.html", context)
