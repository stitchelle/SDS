import sqlite3
from django.shortcuts import redirect, render, reverse
from sdsapp.models import Project
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def my_project_list(request):
    if request.method == 'GET':
        current_user = request.user.teacher_parent

        all_my_projects = Project.objects.filter(teacher_parent_id=current_user.id)
        grade_id = request.GET.get('grade', None)
        subject_id = request.GET.get('subject',None)

        template = 'my_projects/list.html'
        context = {
            'all_my_projects': all_my_projects
        }

        return render(request, template, context)
    