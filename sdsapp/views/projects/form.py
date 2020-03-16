import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sdsapp.models import TeacherParent
from sdsapp.models import Subject
from sdsapp.models import Grade
from sdsapp.models import Project
from sdsapp.models import model_factory
from ..connection import Connection


def get_projects():
    return Project.objects.all()

def get_teacher_parents():
    return TeacherParent.objects.all()

def get_subjects():
    return Subject.objects.all()

def get_grades():
    return Grade.objects.all()

@login_required
def project_form(request):
    if request.method == 'GET':
        projects = get_projects()
        teacher_parents = get_teacher_parents()
        subjects = get_subjects
        grades = get_grades
        template = 'projects/form.html'
        context = {
            'all_projects': projects,
            'all_teacher_parents': teacher_parents,
            'all_subjects': subjects,
            'all_grades': grades
        }

        return render(request, template, context)