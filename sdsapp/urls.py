from django.urls import path
from .views import *

app_name = "sdsapp"

urlpatterns = [
    path('', project_list, name='home'),
    path('projects/', project_list, name='projects'),
    path('grades/', grade_list, name='grades'),
    path('instructions/', instruction_list, name='instructions'),
    path('teacher_parents/', teacher_parent_list, name='teacher_parents'),
    path('subjects/', subject_list, name='subjects'),
]