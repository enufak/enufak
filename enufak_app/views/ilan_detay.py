from django.shortcuts import render, get_object_or_404
from enufak_app.models import Ilan, CustomUser


def ilan_detay(request, userslug, slug):
    author = get_object_or_404(CustomUser, slug=userslug)
    ilan = get_object_or_404(Ilan, slug=slug, ilan_sahibi=author)

    ilan.goruntulenme_sayisi += 1
    ilan.save(update_fields=['goruntulenme_sayisi'])

    return render(request, 'app/ilan_detay.jinja', context={
        'ilan':ilan,
    })