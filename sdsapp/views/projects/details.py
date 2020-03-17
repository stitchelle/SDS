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
        template_name = 'projects/detail.html'
        return render(request, template_name, {'project': project})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a project
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            
            # # retrieve it first:
            project_to_update = Project.objects.get(pk=project_id)

            # # Reassign a property's value
            project_to_update.name = form_data['project']
            project_to_update.subject_id = form_data['subject']
            project_to_update.grade_id = form_data['grade']
            project_to_update.supplies_needed = form_data['supplies']
            project_to_update.description = form_data['description']
            project_to_update.instruction = form_data['instruction']


            # # Save the change to the db
            project_to_update.save()

            return redirect(reverse('sdsapp:projects'))

        # Check if this POST is for deleting a project
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):      
            project = Project.objects.get(pk=project_id)
            project.delete()

            return redirect(reverse('sdsapp:projects'))