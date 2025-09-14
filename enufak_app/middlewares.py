from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

User = get_user_model()


class LastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            User.objects.filter(pk=request.user.pk).update(last_seen=timezone.now())

        return response
    
class TcVerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        if request.user.is_superuser or request.user.is_staff:
            return self.get_response(request)

        ilan_olustur_path = reverse("ilan_ekle")
        tc_dogrulama_path = reverse("tc_dogrulama")
        cikis_yap_path = reverse("cikis_yap")

        if not request.user.tc_verified:
            if request.path.startswith(ilan_olustur_path):
                messages.info(request, 'İlan oluşturabilmek için kimlik doğrulaması yapman gerekmektedir.')
                return redirect("tc_dogrulama")

            if request.path.startswith(tc_dogrulama_path) or request.path.startswith(cikis_yap_path):
                return self.get_response(request)

        return self.get_response(request)