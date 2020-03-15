import sqlite3
from django.shortcuts import render
from django.shortcuts import redirect, render, reverse
from sdsapp.models import TeacherParent
from ..connection import Connection


def teacher_parent_list(request):
    if request.method == 'GET':

        # ******** using SQL **********

        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                tp.id,
                tp.isTeacher,
                tp.user_id,
                u.first_name,
                u.last_name,
                u.username
            from sdsapp_teacherparent tp
            JOIN auth_user u 
            on u.id = tp.user_id
            """)

            all_teacherparents = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                teacherparent = TeacherParent()
                teacherparent.id = row['id']
                teacherparent.isTeacher = row['isTeacher']
                teacherparent.user_id = row ['user_id']

                all_teacherparents.append(teacherparent)

        # ********* using ORM **********

        # all_teacherparents = TeacherParent.objects.all()

        # user_id = request.GET.get('user_id', None)

        template = 'teacher_parents/list.html'
        context = {
            'all_teacherparents': all_teacherparents
        }

        return render(request, template, context)
    