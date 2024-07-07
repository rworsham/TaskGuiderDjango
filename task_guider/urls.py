from django.urls import path
from . import views


app_name = "TaskGuider"
urlpatterns = [
    path("", views.test, name="test"),
    path("dashboard", views.dashboard, name="Dashboard"),
]
