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

        all_teacher_parents = TeacherParent.objects.all()

        user_id = request.GET.get('user_id', None)

        template = 'teacher_parents/list.html'
        context = {
            'all_teacher_parents': all_teacher_parents
        }

        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        # instantiate...
        new_teacher_parent = TeacherParent(
            user_id = request.user.id,
            is_teacher = form_data['is_teacher'],
        )

        # and then save to the db
        print(new_teacher_parent)
        new_teacher_parent.save()

    