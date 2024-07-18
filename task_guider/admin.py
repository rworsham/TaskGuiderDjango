from django.contrib import admin
from .models import TaskPost, Project, WorkState, TaskType


class TaskPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title",)
    search_fields = ("title", "date_created")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)


class WorkStateAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(TaskPost, TaskPostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(WorkState, WorkStateAdmin)
admin.site.register(TaskType, TaskTypeAdmin)
