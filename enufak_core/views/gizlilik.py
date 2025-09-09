from django.shortcuts import render


def gizlilik(request):
    return render(request, 'core/gizlilik.jinja')