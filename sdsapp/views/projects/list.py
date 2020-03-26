import sqlite3
from django.shortcuts import redirect, render, reverse
from sdsapp.models import Project
from sdsapp.models import Dashboard
from sdsapp.models import SavedProject
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def project_list(request):
    if request.method == 'GET':
        current_user = request.user.teacher_parent

        all_projects = Project.objects.all()
        grade_id = request.GET.get('grade', None)

        subject_id = request.GET.get('subject',None)

        all_saved_projects = SavedProject.objects.all()

        all_dashboards = Dashboard.objects.filter(teacher_parent_id=current_user.id)

        template = 'projects/list.html'
        context = {
            'all_projects': all_projects,
            'all_dashboards': all_dashboards,
            'all_saved_projects': all_saved_projects
        }

        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

         # Check if this POST is for actual_method is a project
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "project"
        ):
            current_user = request.user.teacher_parent

            # instantiate...
            new_project = Project(
                name = form_data['project'],
                supplies_needed = form_data['supplies'],
                description = form_data['description'],
                instruction = form_data['instruction'],
                grade_id = form_data["grade"],
                subject_id = form_data["subject"],
                teacher_parent_id = current_user.id,
                image_path = form_data ['image_path']
            )

            # and then save to the db
            print(new_project.name)
            new_project.save()

            return redirect(reverse('sdsapp:projects'))

        # Check if this POST is for adding project to dashboard
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "saved_project"
        ):
            new_saved_project = SavedProject(
            project_id = form_data['project'],
            dashboard_id =form_data['dashboard'],
            note = form_data['note']
        )

        new_saved_project.save()

        return redirect(reverse('sdsapp:projects'))
