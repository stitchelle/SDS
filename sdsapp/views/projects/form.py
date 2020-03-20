import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sdsapp.models import Teacher_Parent
from sdsapp.models import Subject
from sdsapp.models import Grade
from sdsapp.models import Project
from sdsapp.models import model_factory
from ..connection import Connection


def get_projects():
    return Project.objects.all()

def get_subjects():
    return Subject.objects.all()

def get_grades():
    return Grade.objects.all()

@login_required
def project_form(request):
    if request.method == 'GET':
        projects = get_projects()
        subjects = get_subjects()
        grades = get_grades()
        template = 'projects/form.html'
        context = {
            'all_projects': projects,
            'all_subjects': subjects,
            'all_grades': grades
        }

        return render(request, template, context)

@login_required
def project_edit_form(request, project_id):

    if request.method == 'GET':
        project = Project.objects.get(pk=project_id)
        subjects = get_subjects()
        grades = get_grades()
        template = 'projects/form.html'
        context = {
            'project': project,
            'all_subjects': subjects,
            'all_grades': grades
        }

        return render(request, template, context)