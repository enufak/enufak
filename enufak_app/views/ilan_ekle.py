from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from enufak_app.forms import IlanEkleForm
from django.contrib import messages

@login_required
def ilan_ekle(request):
    if request.method == "POST":
        form = IlanEkleForm(request.POST)
        if form.is_valid():
            ilan = form.save(commit=False)
            ilan.ilan_sahibi = request.user 
            ilan.save()
            messages.success(request, 'İlanınız başarıyla oluşturuldu. Sistem tarafından onaylandıktan sonra profilinize eklenecektir.')
            return redirect("profil")
    else:
        form = IlanEkleForm()

    return render(request, "app/ilan_ekle.jinja", {"form": form})