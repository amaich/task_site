from django.contrib import admin

from .models import *

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ("task_name", "task_description", "task_reporter", "task_executor", "task_status")
    
    def get_queryset(self, request):
        return Tasks.objects.select_related("task_reporter")
    




# Register your models here.
