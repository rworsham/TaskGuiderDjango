from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.utils import timezone
from .models import Project, TodoPost, WorkState, TaskType, Comment
from .forms import TaskForm, WorkStateCreateForm
import json
import plotly.express as px
from django.db import connection
import pandas as pd


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
               'work_states': list(WorkState.objects.all()), 'tasks': list(TodoPost.objects.all())}
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        work_state_create_form = WorkStateCreateForm(request.POST)
        if not task_form.is_valid():
            print("task form not valid")
            print(task_form.errors)
            return HttpResponseRedirect("#")
        elif task_form.is_valid():
            new_task = TodoPost()
            new_task.title = task_form.cleaned_data["title"]
            new_task.subtitle = task_form.cleaned_data["subtitle"]
            new_task.work_state = task_form.cleaned_data["work_state"]
            new_task.body = task_form.cleaned_data["body"]
            new_task.due_date = task_form.cleaned_data["due_date"]
            new_task.show_on_calendar = task_form.cleaned_data["show_on_calendar"]
            new_task.type = task_form.cleaned_data["type"]
            new_task.project = task_form.cleaned_data["project"]
            new_task.author = request.user
            new_task.save()
            return HttpResponseRedirect("#")
        elif work_state_create_form.is_valid():
            new_work_state = WorkState()
            new_work_state.name = work_state_create_form.cleaned_data["name"]
            new_work_state.position = work_state_create_form.cleaned_data["position"]
            new_work_state.is_hidden = work_state_create_form.cleaned_data["is_hidden"]
            new_work_state.save()
            return HttpResponseRedirect("#")
    else:
        task_form = TaskForm()
        work_state_create_form = WorkStateCreateForm()
        return render(request, "dashboard.html", context)


def events(request):
    pass


def login(request):
    pass


def overview(request):
    bar_chart = bar_chart_todo()
    return render(request, 'overview.html', {bar_chart: bar_chart})


def bar_chart_todo(request):
    # Query TodoPost and WorkState data
    with connection.cursor() as cursor:
        cursor.execute("SELECT work_state, COUNT(*) AS count FROM yourapp_todopost GROUP BY work_state")
        todo_data = cursor.fetchall()

    cursor.execute("SELECT work_state FROM yourapp_workstate ORDER BY work_state_order")
    work_state_data = cursor.fetchall()

    # Convert query results to DataFrame
    df_todo_count = pd.DataFrame(todo_data, columns=['work_state', 'count'])
    df_work_state = pd.DataFrame(work_state_data, columns=['work_state'])

    # Join DataFrames
    df_graph = df_work_state.merge(df_todo_count, on='work_state', how='left').fillna(0)

    # Create Plotly figure
    fig = px.bar(df_graph, x='work_state', y='count', labels={'work_state': 'Work State', 'count': '# of Tasks'},
                 barmode='group')
    fig.update_layout(yaxis_range=[0, 20])
    fig.update_traces(marker_color='green')

    # Convert plotly figure to JSON
    graphJSON = fig.to_json()

    # Return JSON response
    return JsonResponse(json.loads(graphJSON))


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
