from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from enufak_app.models import AliciTalebi, Ilan
from django.db.models import Q

@login_required
def alici_talepleri(request):
    ilanlar = Ilan.objects.filter(ilan_sahibi=request.user)

    if not ilanlar.exists():
        messages.error(request, "Alıcı taleplerini görebilmek için önce bir ilan oluşturmalısınız.")
        return redirect('ilan_ekle')

    kelimeler = []
    for ilan in ilanlar:
        kelimeler += ilan.ilan_baslik.lower().split()
        kelimeler += ilan.ilan_metni.lower().split()
        if hasattr(ilan, 'etiketler') and ilan.etiketler:
            kelimeler += [e.lower() for e in ilan.etiketler.split(',')]

    filtre = Q()
    for kelime in kelimeler:
        kelime = kelime.strip()
        if kelime:
            filtre |= Q(baslik__icontains=kelime) | Q(metin__icontains=kelime)

    talepler = AliciTalebi.objects.filter(filtre).order_by('-created_at').distinct()

    context = {
        'ilanlar': ilanlar,
        'talepler': talepler
    }
    return render(request, 'app/alici_talepleri.jinja', context)
