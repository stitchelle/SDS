import sqlite3
from django.shortcuts import render
from django.shortcuts import redirect, render, reverse
from sdsapp.models import TeacherParent
from ..connection import Connection


def teacher_parent_list(request):
    if request.method == 'GET':

        # ******** using SQL **********

        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     select
        #         tp.id,
        #         tp.isTeacher
        #         tp.user_id
        #     from sdsapp_teacher_parent tp
        #     """)

        #     all_teacher_parents = []
        #     dataset = db_cursor.fetchall()

        #     for row in dataset:
        #         teacher_parent = TeacherParent()
        #         teacher_parent.id = row['id']
        #         teacher_parent.isTeacher = row['isTeacher']
        #         teacher_parent.user_id = row ['user_id']

        #         all_teacher_parents.append(teacher_parent)

        # ********* using ORM **********

        all_teacher_parents = TeacherParent.objects.all()

        user_id = request.GET.get('user_id', None)

        template = 'teacher_parents/list.html'
        context = {
            'all_teacher_parents': all_teacher_parents
        }

        return render(request, template, context)
    