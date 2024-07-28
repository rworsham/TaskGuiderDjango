from django.urls import path
from . import views


app_name = "task_guider"
urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("events", views.events, name="events"),
    path("login", views.login, name="login"),
    path("overview", views.overview, name="overview"),
    path("project_view/<int:id>/", views.project_view, name="project_view"),
    path("projects", views.projects, name="projects"),
    path("register", views.register, name="register"),
    path("settings", views.settings, name="settings"),
    path("task/<int:id>/", views.task, name="task"),
    path("download/<int:task_id>/<int:file_id>/", views.download_file, name="download"),
    path("calendar", views.calendar, name="calendar"),
    path("logout", views.logout, name="logout"),
]
