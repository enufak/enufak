from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from enufak_app.forms import ProfilDuzenleForm

@login_required
def profil_duzenle(request):
    if request.method == "POST":
        form = ProfilDuzenleForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profil")
    else:
        form = ProfilDuzenleForm(instance=request.user)
    return render(request, "app/profil_duzenle.jinja", {"form": form})
