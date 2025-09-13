from django.shortcuts import get_object_or_404, render, redirect
from enufak_app.models import CustomUser, Ilan


def kullanici(request, slug):
    user = get_object_or_404(CustomUser, slug=slug)
    ilanlar = Ilan.objects.filter(ilan_sahibi=user, aktif=True)

    user.goruntulenme_sayisi += 1
    user.save(update_fields=['goruntulenme_sayisi'])

    if user != request.user:
        return render(request, 'app/kullanici.jinja', context={
            'user':user,
            'ilanlar':ilanlar,
        })
    else:
        return redirect('profil')