from django.urls import include, path
from .views import *

app_name = "sdsapp"

urlpatterns = [
    path('', home, name='home'),
    path('projects/', project_list, name='projects'),
    path('grades/', grade_list, name='grades'),
    path('instructions/', instruction_list, name='instructions'),
    path('teacher_parents/', teacher_parent_list, name='teacher_parents'),
    path('subjects/', subject_list, name='subjects'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),

    path('subject/form', subject_form, name='subject_form'),

]