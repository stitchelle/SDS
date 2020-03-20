from django.urls import include, path
from .views import *
from django.urls import path


app_name = "sdsapp"

urlpatterns = [
    path('', home, name='home'),
    path('projects/', project_list, name='projects'),
    path('grades/', grade_list, name='grades'),
    path('instructions/', instruction_list, name='instructions'),
    path('teacher_parents/', teacher_parent_list, name='teacher_parents'),
    path('subjects/', subject_list, name='subjects'),
    path('my_projects/', my_project_list, name='my_projects'),

    
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name="register"),
    path('logout/', logout_user, name='logout'),


    path('subject/form', subject_form, name='subject_form'),
    path('project/form', project_form, name='project_form'),

    # The <int:project_id> part of that URL pattern is used to capture any integer that is the route parameter, and stores that number in the project_id variable.
    path('projects/<int:project_id>/', project_details, name='project'),

    path('projects/<int:project_id>/form/', project_edit_form, name='project_edit_form'),


]