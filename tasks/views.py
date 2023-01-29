from django.shortcuts import render
from django.views import generic

from .models import *
# Create your views here.


class TaskListView(generic.ListView):
    model = Tasks
    context_object_name = "tasks"

class TaskDetailView(generic.DetailView):
    model = Tasks
    context_object_name = "task"
