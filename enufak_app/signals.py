from django.dispatch import receiver
from allauth.account.signals import user_signed_up, user_logged_in

@receiver(user_signed_up)
def set_email_verified_on_signup(request, user, **kwargs):
    user.email_verified = True
    user.is_active = True
    user.save()

@receiver(user_logged_in)
def ensure_verified_on_login(request, user, **kwargs):
    if not user.email_verified:
        user.email_verified = True
        user.is_active = True
        user.save()