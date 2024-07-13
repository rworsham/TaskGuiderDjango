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
