from django.shortcuts import render
from enufak_app.models import Ilan

def index(request):
    ilanlar = Ilan.objects.filter(aktif=True)
    return render(request, 'app/kesfet.jinja', context={
        'ilanlar':ilanlar,
    })