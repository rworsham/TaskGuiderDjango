from django import forms
from django.forms import ModelForm
from .models import WorkState, TaskType, Project, Comment, TaskPost
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CreateTaskForm(forms.Form):
    title = forms.CharField(label="Title", required=True, max_length=100)
    subtitle = forms.CharField(label="Subtitle", required=True, max_length=100)
    work_state = forms.ModelChoiceField(label="Select Work State",
                                        queryset=WorkState.objects.all(), to_field_name='name', required=True)
    body = forms.CharField(label="Content", widget=forms.Textarea(attrs={'name': 'body', 'rows': '3', 'cols': '5'}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    show_on_calendar = forms.BooleanField(label="Show on Calendar?")
    type = forms.ModelChoiceField(label="Select Task Type if applicable",
                                  queryset=TaskType.objects.all(), to_field_name='name', required=True)
    project = forms.ModelChoiceField(label="Select Project",
                                     queryset=Project.objects.all(), to_field_name='name', required=True)


class EditTaskForm(ModelForm):
    class Meta:
        model = TaskPost
        fields = ["title", "subtitle", "work_state", "body", "due_date", "show_on_calendar", "type", "project_name"]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)


class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Email Address", required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}), required=True)
    name = forms.CharField(max_length=100, required=True)
    is_admin = forms.BooleanField(label="Set Admin")


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        labels = {
            "body": _("Comments"),
        }


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "color"]


class WorkStateCreateForm(ModelForm):
    class Meta:
        model = WorkState
        fields = ["name", "position", "is_hidden"]
        labels = {
            "is_hidden": _("Visibility"),
        }


class WorkStateEditForm(ModelForm):
    class Meta:
        model = WorkState
        fields = ["position", "is_hidden"]
        labels = {
            "is_hidden": _("Visibility"),
        }


class WorkStateChangeFrom(forms.Form):
    new_work_state = forms.ModelChoiceField(label="Select Work State",
                                        queryset=WorkState.objects.all(), to_field_name='name', required=True)


class TaskTypeForm(ModelForm):
    class Meta:
        model = TaskType
        fields = ["name", "icon"]
        labels = {
            "name": _("Task Type Name"),
        }


class RegisterNewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff", "password"]
        labels = {

        }
