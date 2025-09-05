from django.shortcuts import get_object_or_404, render
from enufak_app.models import CustomUser, Ilan


def kullanici(request, slug):
    user = get_object_or_404(CustomUser, slug=slug)
    ilanlar = Ilan.objects.filter(ilan_sahibi=user, aktif=True)

    return render(request, 'app/kullanici.jinja', context={
        'user':user,
        'ilanlar':ilanlar,
    })