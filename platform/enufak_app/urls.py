from django.urls import path
from enufak_app.views import *
from django.shortcuts import redirect


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

    #
    path('@<slug:slug>/', kullanici, name='kullanici'),
]