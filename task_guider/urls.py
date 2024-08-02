from django.urls import path
from . import views


app_name = "task_guider"
urlpatterns = [
    path("", views.login_page, name="login_page"),
    path("accounts/login/", views.login_page),
    path("dashboard", views.dashboard, name="dashboard"),
    path("events", views.events, name="events"),
    path("event_data", views.events, name="event_data"),
    path("overview", views.overview, name="overview"),
    path("project_view/<int:id>/", views.project_view, name="project_view"),
    path("projects", views.projects, name="projects"),
    path("register", views.register_user, name="register"),
    path("settings", views.settings, name="settings"),
    path("task/<int:id>/", views.task, name="task"),
    path("download/<int:task_id>/<int:file_id>/", views.download_file, name="download"),
    path("logout_user", views.logout_user, name="logout_user"),
]
