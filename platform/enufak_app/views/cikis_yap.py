from django.shortcuts import redirect
from django.contrib.auth import logout

def cikis_yap(request):
    logout(request)
    return redirect('giris_yap')