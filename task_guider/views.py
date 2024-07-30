from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.db.models import F, Q
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project, TaskPost, WorkState, TaskType, Comment
from .forms import CreateTaskForm, WorkStateCreateForm, EditTaskForm, WorkStateChangeFrom, CommentForm, ProjectForm, LoginForm
from subscribed.models import Subscribed
import json
import plotly.express as px
from django.db import connection
import pandas as pd


def login_page(request):
    context = {"login_form": LoginForm()}
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if "login_request" in request.POST:
            if not login_form.is_valid():
                print(login_form.errors)
                HttpResponseRedirect("#")
            elif login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('task_guider:dashboard')
                else:
                    print("user is none or incorrect creds")
                    HttpResponseRedirect("#")
    else:
        login_form = LoginForm()
        return render(request, "login.html", context)


@login_required
def dashboard(request):
    context = {'task_form': CreateTaskForm(), "work_state_create_form": WorkStateCreateForm(),
               'work_states': list(WorkState.objects.all()), 'tasks': list(TaskPost.objects.all())}
    if request.method == "POST":
        task_form = CreateTaskForm(request.POST)
        work_state_create_form = WorkStateCreateForm(request.POST)
        if "task_form" in request.POST:
            if not task_form.is_valid():
                print(task_form.errors)
                return HttpResponseRedirect("#")
            elif task_form.is_valid():
                new_task = TaskPost()
                new_task.title = task_form.cleaned_data["title"]
                new_task.subtitle = task_form.cleaned_data["subtitle"]
                new_task.work_state = task_form.cleaned_data["work_state"]
                new_task.body = task_form.cleaned_data["body"]
                new_task.due_date = task_form.cleaned_data["due_date"]
                new_task.show_on_calendar = task_form.cleaned_data["show_on_calendar"]
                new_task.type = task_form.cleaned_data["type"]
                new_task.project_name = task_form.cleaned_data["project"]
                new_task.author = request.user
                new_task.save()
                return HttpResponseRedirect("#")
        if "workstate_form" in request.POST:
            if not work_state_create_form.is_valid():
                print(work_state_create_form.errors)
                return HttpResponseRedirect("#")
            elif work_state_create_form.is_valid():
                new_work_state = WorkState()
                new_work_state.name = work_state_create_form.cleaned_data["name"]
                new_work_state.position = work_state_create_form.cleaned_data["position"]
                new_work_state.is_hidden = work_state_create_form.cleaned_data["is_hidden"]
                new_work_state.save()
                return HttpResponseRedirect("#")
    else:
        task_form = CreateTaskForm()
        work_state_create_form = WorkStateCreateForm()
        return render(request, "dashboard.html", context)


@login_required
def events(request):
    context = {}
    return render(request, "events.html", context)


@login_required
def overview(request):
    bar_chart = bar_chart_todo()
    return render(request, 'overview.html', {bar_chart: bar_chart})


@login_required
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


@login_required
def project_view(request, id):
    project = get_object_or_404(Project, id=id)
    context = {"project": project, "work_state": list(WorkState.objects.all())}
    return render(request, "project_view.html", context)


@login_required
def projects(request):
    context = {"projects": list(Project.objects.all()), "project_form": ProjectForm()}
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if "project_form" in request.POST:
            if not project_form.is_valid():
                print(project_form.errors)
                return HttpResponseRedirect('#')
            elif project_form.is_valid():
                project_form.save()
                return HttpResponseRedirect('#')
    else:
        project_form = ProjectForm()
        return render(request, "projects.html", context)


@login_required
def register(request):
    pass


@login_required
def settings(request):
    pass


@login_required
def task(request,id):
    task_post = get_object_or_404(TaskPost, id=id)
    is_subscribed = Subscribed.objects.filter(Q(email=request.user) & Q(subscribed_object=task_post)).exists()
    print(is_subscribed)
    context = {'task': task_post, "task_edit_form": EditTaskForm(), "work_state_change_form": WorkStateChangeFrom(),
               "comments": list(Comment.objects.filter(parent_post=id)), "comment_form": CommentForm(),
               "subscription_status": is_subscribed}
    if request.method == "POST":
        task_edit_form = EditTaskForm(request.POST)
        work_state_change_form = WorkStateChangeFrom(request.POST)
        comment_form = CommentForm(request.POST)
        if "task_edit_form" in request.POST:
            if not task_edit_form.is_valid():
                print(task_edit_form.errors)
                return HttpResponseRedirect('#')
            elif task_edit_form.is_valid():
                task_edit_form.save()
                return HttpResponseRedirect('#')
        if "work_state_change_form" in request.POST:
            if not work_state_change_form.is_valid():
                print(work_state_change_form.errors)
                return HttpResponseRedirect('#')
            elif work_state_change_form.is_valid():
                new_work_state = task_post
                new_work_state.work_state = work_state_change_form.cleaned_data['new_work_state']
                new_work_state.save()
                return HttpResponseRedirect('#')
        if "comment_form" in request.POST:
            if not comment_form.is_valid():
                print(comment_form.errors)
                return HttpResponseRedirect('#')
            elif comment_form.is_valid():
                new_comment = Comment()
                new_comment.body = comment_form.cleaned_data['body']
                new_comment.author = request.user
                new_comment.parent_post = task_post
                new_comment.save()
                return HttpResponseRedirect('#')
        if "subscribe" in request.POST:
            subscribe_user = Subscribed()
            subscribe_user.email_id = request.user.id
            subscribe_user.subscribed_object_id = task_post.id
            subscribe_user.save()
            print("sub")
            return HttpResponseRedirect('#')
        if "unsubscribe" in request.POST:
            unsubscribe_user = Subscribed.objects.filter(Q(email=request.user.id) & Q(subscribed_object=task_post.id))
            unsubscribe_user.delete()
            print("unsub")
            return HttpResponseRedirect('#')
    else:
        task_edit_form = EditTaskForm()
        work_state_change_form = WorkStateChangeFrom()
        comment_form = CommentForm()
        return render(request, "task.html", context)


@login_required
def calendar(request):
    pass


@login_required
def logout_user(request):
    logout(request)
    return redirect("task_guider:login_page")


@login_required
def download_file(request,task_id,file_id):
    task = get_object_or_404(TaskPost, pk=task_id)
#    file = get_object_or_404() decide where files are served from
    return HttpResponseRedirect("#")
