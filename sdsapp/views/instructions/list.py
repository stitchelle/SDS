import sqlite3
from django.shortcuts import redirect, render, reverse
from sdsapp.models import Instruction
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def instruction_list(request):
    if request.method == 'GET':
        all_instructions = Instruction.objects.all()

        template = 'instructions/list.html'
        context = {
            'all_instructions': all_instructions
        }

        return render(request, template, context)