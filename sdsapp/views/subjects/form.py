import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sdsapp.models import Subject
from sdsapp.models import model_factory
from ..connection import Connection

def get_subjects():
    return Subject.objects.all()

@login_required
def subject_form(request):
    if request.method == 'GET':
        subjects = get_subjects()
        template = 'subjects/form.html'
        context = {
            'all_subjects': subjects
        }

        return render(request, template, context)