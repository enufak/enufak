from django.shortcuts import render
from enufak_blog.models import Gonderi

def index(request):
    gonderiler = Gonderi.objects.order_by('-id')[:3]

    return render(request, 'core/index.jinja', context={
        'gonderiler':gonderiler,
    })