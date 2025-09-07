from django.shortcuts import render, redirect
from enufak_app.forms import AliciTalebiForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages


@login_required
def alici_talebi_olustur(request):
    bir_gun_once = timezone.now() - timedelta(days=1)
    son_talepler = request.user.alicitalebi_set.filter(created_at__gte=bir_gun_once)

    if request.method == 'POST':
        if son_talepler.count() >= 2:
            messages.error(request, "Son 24 saat içinde maksimum 2 alıcı talebi oluşturabilirsiniz.")
            return redirect('app_index')

        form = AliciTalebiForm(request.POST)
        if form.is_valid():
            talep = form.save(commit=False)
            talep.yazar = request.user
            talep.save()
            messages.success(request, "Alıcı talebiniz oluşturuldu!")
            return redirect('app_index')
    else:
        form = AliciTalebiForm()
    
    return render(request, 'app/talep_olustur.jinja', {'form': form})