from django.shortcuts import render
from django.views import generic

from .models import *
# Create your views here.

def visit_count(request):
    session_count = request.session.get('visits', 0)
    request.session['visits'] = session_count + 1

class TaskListView(generic.ListView):
    model = Tasks
    context_object_name = "tasks"
    
    def get_context_data(self):
        context = super(TaskListView,self).get_context_data()
        context['test'] = dir(self.request)
        context['visit_count'] = self.request.session['visits']
        return context

    def get(self, request):
        visit_count(self.request)
        return super().get(request)    


class TaskDetailView(generic.DetailView):
    model = Tasks
    context_object_name = "task"

def session_test(request):
    all_request_defs = dir(request)

    if request.session.get('newbee') == None:
        greetings = 'Hello, Stranger!'
        request.session['newbee'] = 1
    else:
        greetings = 'Welcome back!'
    all_session_params = dict(request.session)
    context = {
        'all_defs': all_request_defs,
        'all_params': all_session_params,
        'greetings': greetings,
        'test_get': request.session.get('pososo')

    }
    return render(request, 'tasks/test.html', context)