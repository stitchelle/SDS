from django.shortcuts import redirect, render, reverse
from sdsapp.models import Subject
from ..connection import Connection


def subject_list(request):
    if request.method == 'GET':
        all_subjects = Subject.objects.all()

        template = 'subjects/list.html'
        context = {
            'all_subjects': all_subjects
        }

        return render(request, template, context)