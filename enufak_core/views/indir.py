from django.shortcuts import render

def indir(request):
    return render(request, 'core/indir.jinja')