import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sdsapp.models import Project
from sdsapp.models import model_factory
from ..connection import Connection


def get_project(project_id):
    return Project.objects.get(pk=project_id)

@login_required
def project_details(request, project_id):
    if request.method == 'GET':
        project = get_project(project_id)

        template = 'projects/detail.html'
        context = {
            'project': project
        }

        return render(request, template, context)