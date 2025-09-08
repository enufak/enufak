from django.urls import path
from enufak_app.views import *
from django.shortcuts import redirect
from allauth.socialaccount.providers.google.views import oauth2_login



urlpatterns = [
    path('kesfet/', index, name='app_index'),
    path('', lambda request: redirect('app_index', permanent=False)),
    path('kayit-ol/', kayit, name='kayit_ol'),
    path('giris-yap/', giris, name='giris_yap'),
    path('cikis-yap/', cikis_yap, name='cikis_yap'),
    path('profil/', profil, name='profil'),
    path('profil/duzenle/', profil_duzenle, name='profil_duzenle'),
    path('ilan-ekle/', ilan_ekle, name='ilan_ekle'),
    path('ara/', ilan_arama, name='ilan_ara'),
    path('alici-talebi-olustur/', alici_talebi_olustur, name='alici_talebi_olustur'),
    path('alici-talepleri/', alici_talepleri, name='alici_talepleri'),
    path('ilan-duzenle/<int:id>/', ilan_duzenle, name='ilan_duzenle'),
    path('ilan-sil/<int:id>/', ilan_sil, name='ilan_sil'),
    path("google/login/", oauth2_login, name="google_login_direct"),
    #
    path('@<slug:slug>/', kullanici, name='kullanici'),
]