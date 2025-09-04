from django.shortcuts import render
from enufak_app.models import Ilan

def index(request):
    ilanlar = Ilan.objects.filter(aktif=True).order_by('-id')[:6]
    return render(request, 'app/kesfet.jinja', context={
        'ilanlar':ilanlar,
    })