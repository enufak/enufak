from django.shortcuts import render


def kullanim_kosullari(request):
    return render(request, 'core/kullanim_kosullari.jinja')