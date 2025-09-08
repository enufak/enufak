from django.shortcuts import render, redirect
from django.contrib.auth import login
from enufak_app.forms import KayitForm

def kayit(request):
    if request.method == "POST":
        form = KayitForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend') 
            return redirect('app_index')
    else:
        form = KayitForm()
    return render(request, 'app/kayit.jinja', {'form': form})
