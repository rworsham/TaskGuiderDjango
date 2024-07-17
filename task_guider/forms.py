from django import forms
from django.forms import ModelForm
from .models import WorkState, TaskType, Project, Comment


class TaskForm(forms.Form):
    title = forms.CharField(label="Title", required=True, max_length=100)
    subtitle = forms.CharField(label="Subtitle", required=True, max_length=100)
    work_state = forms.ModelChoiceField(label="Select Work State",
                                        queryset=WorkState.objects.all(), to_field_name='name', required=True)
    body = forms.CharField(label="Content", widget=forms.Textarea(attrs={'name': 'body', 'rows': '3', 'cols': '5'}))
    due_date = forms.DateField()
    show_on_calendar = forms.BooleanField(label="Show on Calendar?")
    type = forms.ModelChoiceField(label="Select Task Type if applicable",
                                  queryset=TaskType.objects.all(), to_field_name='name', required=True)
    project = forms.ModelChoiceField(label="Select Project",
                                     queryset=Project.objects.all(), to_field_name='name', required=True)


class TaskEditForm(forms.Form):
    title = forms.CharField(label="Title", required=True, max_length=100)
    subtitle = forms.CharField(label="Subtitle", required=True, max_length=100)
    work_state = forms.ModelChoiceField(label="Select Work State",
                                        queryset=WorkState.objects.values_list('name', flat=True), required=True)
    body = forms.CharField(label="Content", widget=forms.Textarea(attrs={'name': 'body', 'rows': '3', 'cols': '5'}))
    due_date = forms.DateField()
    show_on_calendar = forms.BooleanField(label="Show on Calendar?")
    type = forms.ModelChoiceField(label="Select Task Type if applicable",
                                  queryset=TaskType.objects.values_list('name', flat=True), required=False)
    project = forms.ModelChoiceField(label="Select Project",
                                     queryset=Project.objects.values_list('name', flat=True), required=True)


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    password = forms.PasswordInput()


class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Email Address", required=True)
    password = forms.PasswordInput()
    name = forms.CharField(max_length=100, required=True)
    is_admin = forms.BooleanField(label="Set Admin")


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "color"]


class WorkStateCreateForm(ModelForm):
    class Meta:
        model = WorkState
        fields = ["name", "position", "is_hidden"]


class WorkStateChangeFrom(forms.Form):
    new_state = forms.ModelChoiceField(label="Select Work State",
                                       queryset=WorkState.objects.values_list("name", flat=True), required=True)


class SubscribeUser(forms.Form):
    pass


class UnsubscribeUserForm(forms.Form):
    pass

