from django.shortcuts import redirect, render, reverse
from sdsapp.models import Subject
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def subject_list(request):
    if request.method == 'GET':
        all_subjects = Subject.objects.all()

        template = 'subjects/list.html'
        context = {
            'all_subjects': all_subjects
        }

        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST
        
        # instantiate...
        new_subject = Subject(
            name = form_data['subject']
        )

        # and then save to the db
        print(new_subject.name)
        new_subject.save()

        return redirect(reverse('sdsapp:subjects'))
