from django import forms
from django.forms import ModelForm
from .models import WorkState, TaskType, Project


class TaskForm(forms.Form):
    title = forms.CharField(label="Title", required=True, max_length=100)
    subtitle = forms.CharField(label="Subtitle", required=True, max_length=100)
    work_state = forms.ModelChoiceField(label="Select Work State", queryset=WorkState.objects.all(),required=True)
    body = forms.CharField(label="Content", widget=forms.Textarea(attrs={'name': 'body', 'rows': '3', 'cols': '5'}))
    due_date = forms.DateField()
    show_on_calendar = forms.BooleanField(label="Show on Calendar?")
    type = forms.ModelChoiceField(label="Select Task Type if applicable", queryset=TaskType.objects.all(), required=False)
    project = forms.ModelChoiceField(label="Select Project", queryset=Project.objects.all(), required=True)


class TaskEditForm(forms.Form):
    pass


class LoginForm(forms.Form):
    pass


class RegistrationForm(forms.Form):
    pass


class CommentForm(forms.Form):
    pass


class ProjectForm(forms.Form):
    pass


class WorkStateCreateForm(forms.Form):
    pass


class WorkStateChangeFrom(forms.Form):
    pass


class WorkStateEditForm(forms.Form):
    pass


class SubscribeUser(forms.Form):
    pass


class UnsubscribeUserForm(forms.Form):
    pass

