from django.shortcuts import render

def profile(request):
    if request.method == 'GET':
        template = 'profile.html'
        context = {}

        return render(request, template, context)