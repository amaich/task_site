from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('test/', views.session_test, name='session_test'),
]