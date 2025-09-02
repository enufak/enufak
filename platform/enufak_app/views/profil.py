from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from enufak_app.models import Ilan


@login_required
def profil(request):
    yeni_kullanici = (timezone.now() - request.user.date_joined) <= timedelta(days=5)
    ilanlar = Ilan.objects.filter(ilan_sahibi=request.user)


    return render(request, 'app/profil.jinja', context={
        'yeni_kullanici':yeni_kullanici,
        'ilanlar':ilanlar,
    })