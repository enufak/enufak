from django.shortcuts import render
from enufak_app.models import Ilan
from django.db.models import Q

def ilan_arama(request):
    kelime = request.GET.get("kelime", "")
    konum = request.GET.get("konum", "")
    min_ucret = request.GET.get("min_ucret")
    max_ucret = request.GET.get("max_ucret")
    secili_kategori = request.GET.get("kategori")
    onayli = request.GET.get('onayli')
    cevrimici = request.GET.get('cevrimici')

    ilanlar = Ilan.objects.filter(aktif=True).order_by('-id')

    if kelime:
        ilanlar = ilanlar.filter(
            Q(ilan_baslik__icontains=kelime) | Q(ilan_metni__icontains=kelime)
        )

    if konum:
        ilanlar = ilanlar.filter(konum__icontains=konum)

    if min_ucret:
        ilanlar = ilanlar.filter(istenilen_ucret__gte=min_ucret)
    if max_ucret:
        ilanlar = ilanlar.filter(istenilen_ucret__lte=max_ucret)
    if onayli == '1':
        ilanlar = ilanlar.filter(ilan_sahibi__onayli_kullanici=True)
    if cevrimici == '1':
        ilanlar = [ilan for ilan in ilanlar if ilan.ilan_sahibi.is_online]

    if secili_kategori:
        ilanlar = ilanlar.filter(kategori=secili_kategori)

    context = {
        "ilanlar": ilanlar,
        "kelime": kelime,
        "konum": konum,
        "min_ucret": min_ucret,
        "max_ucret": max_ucret,
        "kategoriler": Ilan.KATEGORI_SECENEKLERI,
        "secili_kategori": secili_kategori,
    }
    return render(request, "app/ara.jinja", context)
