from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

from enufak_app.models import Ilan
from enufak_app.forms import IlanEkleForm


@login_required
def ilan_duzenle(request, id):
    ilan = get_object_or_404(Ilan, id=id)

    if ilan.ilan_sahibi != request.user:
        return HttpResponseForbidden("Bu ilanı düzenleme yetkiniz yok.")

    if request.method == "POST":
        form = IlanEkleForm(request.POST, request.FILES, instance=ilan)
        if form.is_valid():
            ilan = form.save(commit=False)
            ilan.aktif = False
            ilan.save()

            messages.success(request, 'İlanınız başarıyla düzenlendi. Sistem tarafından onaylanınca profilinize yansıyacaktır.')
            return redirect("profil")
    else:
        form = IlanEkleForm(instance=ilan)

    return render(request, "app/ilan_duzenle.jinja", {"form": form, "ilan": ilan})
