from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site


def send_verification_email(request, user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    domain = get_current_site(request).domain
    scheme = "https" if request.is_secure() else "http"
    verify_url = f"{scheme}://{domain}{reverse('hesap_dogrula', kwargs={'uidb64': uidb64, 'token': token})}"

    subject = "Enufak | E-posta Doğrulama"
    text_body = f"Hesabınızı doğrulamak için linke tıklayın:\n{verify_url}"
    html_body = f"""
    <p>Merhaba {user.get_full_name() or user.first_name},</p>
    <p>Hesabınızı doğrulamak için lütfen aşağıdaki bağlantıya tıklayın:</p>
    <p><a href="{verify_url}">{verify_url}</a></p>
    <p>Teşekkürler,<br>Enufak Ekibi</p>
    """

    msg = EmailMultiAlternatives(subject, text_body, to=[user.email])
    msg.attach_alternative(html_body, "text/html")
    msg.send()
