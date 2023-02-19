from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "start_time",
        "status",
        "end_time",
    )
    readonly_fields = ["start_time", "end_time"]
    list_filter = ["status"]
    search_fields = ("name",)
