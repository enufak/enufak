from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from enufak_app.models import Ilan
from django.shortcuts import render


@login_required
def ilan_sil(request, id):
    ilan = get_object_or_404(Ilan, id=id)

    if ilan.ilan_sahibi != request.user:
        return HttpResponseForbidden("Bu ilanı silme yetkiniz yok.")

    ilan.delete()
    messages.success(request, "İlanınız başarıyla silindi.")
    return redirect("profil")