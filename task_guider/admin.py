from django.contrib import admin
from .models import TodoPost, Project


class TodoPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title",)
    search_fields = ("title", "date_created")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)


admin.site.register(TodoPost, TodoPostAdmin)
admin.site.register(Project, ProjectAdmin)
