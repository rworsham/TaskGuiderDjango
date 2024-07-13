from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.utils import timezone
from .models import Project, TodoPost, WorkState, TaskType, Comment
from .forms import TaskForm, WorkStateCreateForm



def test(request):
    context = {'form': TaskForm()}
    # if form.is_valid():
    #     for x in form.cleaned_data:
    #         print(x)
    # else:
    #     return render(request, "task_guider/test.html")
    return render(request, "test.html", context)


def dashboard(request):
    context = {'task_form': TaskForm(), "work_state_create_form": WorkStateCreateForm(),
               'work_states': WorkState.objects.values_list('name', flat=True)}
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        work_state_create_form = WorkStateCreateForm(request.POST)
        if task_form.is_valid():
            print(task_form.cleaned_data["title"])
            print(task_form.cleaned_data["subtitle"])
            print(task_form.cleaned_data["project"])
            return HttpResponseRedirect("#")
        elif work_state_create_form.is_valid():
            print(work_state_create_form.cleaned_data["name"])
            return HttpResponseRedirect("#")
    else:
        task_form = TaskForm()
        work_state_create_form = WorkStateCreateForm()
    print(request.POST)
    return render(request, "dashboard.html", context)


def events(request):
    pass


def login(request):
    pass


def overview(request):
    pass


def project_view(request):
    pass


def projects(request):
    pass


def register(request):
    pass


def settings(request):
    pass


def task(request):
    pass


def calendar(request):
    pass


def logout(request):
    pass
