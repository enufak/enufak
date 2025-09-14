from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse

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

        if not request.user.tc_verified and request.path not in [
            reverse("tc_dogrulama"),
            reverse("cikis_yap"),
        ]:
            return redirect("tc_dogrulama")

        return self.get_response(request)