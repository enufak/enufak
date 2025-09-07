from django.shortcuts import render
from enufak_app.models import Ilan
from django.core.paginator import Paginator


def index(request):
    ilan_liste = Ilan.objects.filter(aktif=True).order_by('-id')
    paginator = Paginator(ilan_liste, 6)
    
    page_number = request.GET.get('sayfa')
    ilanlar = paginator.get_page(page_number)

    kategori_sayilari = {
        'egitim': ilan_liste.filter(kategori='egitim').count(),
        'teknoloji': ilan_liste.filter(kategori='teknoloji').count(),
        'eglence': ilan_liste.filter(kategori='eglence').count(),
        'moda': ilan_liste.filter(kategori='moda').count(),
    }


    return render(request, 'app/kesfet.jinja', context={
        'ilanlar':ilanlar,
        'kategori_sayilari':kategori_sayilari,
    })