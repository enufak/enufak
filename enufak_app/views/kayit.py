from django.shortcuts import render, redirect
from enufak_app.forms import KayitForm
from enufak_app.utils import send_verification_email
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
import requests
from django.conf import settings
from enufak_app.utils import turkce_upper



User = get_user_model()


def kayit(request):
    if request.method == "POST":
        form = KayitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            user = form.save(commit=False)
            user.is_active = False
            user.email_verified = False
            user.save()

            send_verification_email(request, user)
            messages.success(request, 'Kayıt başarılı! Lütfen e-postanızı doğrulayın.')
            return redirect('giris_yap')
        else:
            return render(request, 'app/kayit.jinja', {'form': form})
    else:
        form = KayitForm()
    return render(request, 'app/kayit.jinja', {'form': form})


def hesap_dogrula(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(User, pk=uid)
    except Exception:
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.email_verified = True
        user.save()
        messages.success(request, "E-posta adresiniz doğrulandı! Artık giriş yapabilirsiniz.")
        return redirect("giris_yap")
    else:
        messages.error(request, "Doğrulama linki geçersiz veya süresi dolmuş.")
        return redirect("giris_yap")