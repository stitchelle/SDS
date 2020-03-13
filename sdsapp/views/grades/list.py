import sqlite3
from django.shortcuts import render
from sdsapp.models import Grade
from ..connection import Connection


def grade_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                g.id,
                g.name
            from sdsapp_grade g
            """)

            all_grades = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                grade = Grade()
                grade.id = row['id']
                grade.name = row['name']

                all_grades.append(grade)

        template = 'grades/list.html'
        context = {
            'all_grades': all_grades
        }

        return render(request, template, context)