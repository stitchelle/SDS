import sqlite3
from django.shortcuts import redirect, render, reverse
from sdsapp.models import Dashboard
from sdsapp.models import SavedProject
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_list(request):
    if request.method == 'GET':
        current_user = request.user.teacher_parent
        
        all_saved_projects = SavedProject.objects.all()

        all_dashboards = Dashboard.objects.filter(teacher_parent_id=current_user.id)
        teacher_parent_id = request.GET.get('teacher_parent',None)

        template = 'dashboards/list.html'
        context = {
            'all_dashboards': all_dashboards,
            'all_saved_projects': all_saved_projects
        }

        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        current_user = request.user.teacher_parent

        # instantiate...
        new_dashboard = Dashboard(
            name = form_data['dashboard'],
            teacher_parent_id = current_user.id,
        )
        new_saved_project = SavedProject(
            project_id = form_data['project'],
            dashboard_id =form_data['dashboard'],
            note = form_data['note']
        )
        # and then save to the db
        print(new_dashboard.name)
        new_dashboard.save()
        new_saved_project()

        return redirect(reverse('sdsapp:dashboards'))