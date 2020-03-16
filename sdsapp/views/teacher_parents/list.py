import sqlite3
from django.shortcuts import render
from django.shortcuts import redirect, render, reverse
from sdsapp.models import TeacherParent
from sdsapp.models import model_factory

from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def teacher_parent_list(request):
    if request.method == 'GET':

        # ******** using SQL **********

        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(TeacherParent)
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

            all_teacherparents = db_cursor.fetchall()

        # ********* using ORM **********

        # all_teacherparents = TeacherParent.objects.all()

        # user_id = request.GET.get('user_id', None)

        template = 'teacher_parents/list.html'
        context = {
            'all_teacherparents': all_teacherparents
        }

        return render(request, template, context)
    