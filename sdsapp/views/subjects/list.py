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

        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     INSERT INTO sdsapp_subject
        #     (
        #         name
        #     )
        #     VALUES (?)
        #     """,
        #     (form_data['name'])
        
        # instantiate...
        new_subject = Subject(
            name = form_data['subject']
        )

        # and then save to the db
        print(new_subject.name)
        new_subject.save()

        # Or...
        # Use a shortcut to do both at the same time
        # new_subject = Subject.objects.create(
        #     name = form_data['name']
        # )

        return redirect(reverse('sdsapp:subjects'))
