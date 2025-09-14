# users/views.py veya enufak_app/views.py
import logging
import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from enufak_app.forms import TcDogrulamaForm
from enufak_app.utils import turkce_upper
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

from django.db import IntegrityError

@login_required
def tc_dogrulama(request):
    if request.method == "POST":
        form = TcDogrulamaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            payload = {
                "tc": data["tckno"],
                "ad": turkce_upper(data["ad"]),
                "soyad": turkce_upper(data["soyad"]),
                "dogumTarihi": data["dogum_tarihi"].strftime("%Y-%m-%d"),
            }

            response = requests.post("https://tc-kimlik.ibrahimo.dev/api/dogrula", json=payload)
            api_data = response.json()

            if api_data.get("result"):
                user = request.user
                try:
                    user.tckno = data["tckno"]
                    user.first_name = data["ad"]
                    user.last_name = data["soyad"]
                    user.dogum_tarihi = data["dogum_tarihi"]
                    user.tc_verified = True
                    user.save()
                    messages.success(request, "TC Kimlik doğrulamanız başarılı!")
                    return redirect("app_index")
                except IntegrityError:
                    messages.error(request, "Bu T.C. Kimlik numarası başka bir kullanıcı tarafından doğrulanmış.")
                    return redirect("tc_dogrulama")
            else:
                messages.error(request, "TC Kimlik doğrulaması başarısız. Lütfen bilgilerinizi kontrol edin.")
                return redirect("tc_dogrulama")
    else:
        form = TcDogrulamaForm()

    return render(request, "app/tc_dogrula.jinja", {"form": form})
