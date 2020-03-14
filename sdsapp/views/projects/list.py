import sqlite3
from django.shortcuts import redirect, render, reverse
from sdsapp.models import Project
from ..connection import Connection


def project_list(request):
    if request.method == 'GET':

        # ******** using SQL ********

        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     select
        #         p.id,
        #         p.name,
        #         p.supplies_needed,
        #         p.description,
        #         p.grade_id,
        #         p.instruction_id,
        #         p.subject_id,
        #         p.teacher_parent_id,
        #         p.image_path
        #     from sdsapp_project p
        #     """)

        #     all_projects = []
        #     dataset = db_cursor.fetchall()

        #     for row in dataset:
        #         project = Project()
        #         project.id = row['id']
        #         project.name = row['name']
        #         project.supplies_needed = row['supplies_needed']
        #         project.description = row['description']
        #         project.grade_id = row['grade_id']
        #         project.instruction_id = row['instruction_id']
        #         project.subject_id = row['subject_id']
        #         project.teacher_parent_id = row['teacher_parent_id']
        #         project.image_path = row['image_path']

        #         all_projects.append(project)
        
        # ********** using ORM ***********

        all_projects = Project.objects.all()

        grade_id = request.GET.get('grade', None)
        instruction_id = request.GET.get('instruction', None)
        subject_id = request.GET.get('subject',None)
        teacher_parent_id = request.GET.get('subject', None)

        template = 'projects/list.html'
        context = {
            'all_projects': all_projects
        }

        return render(request, template, context)