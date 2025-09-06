from django.urls import path
from enufak_mesaj.views import *


urlpatterns = [
    path('', mesajlarim, name='mesajlarim'),
    path('dm-olustur/<str:ids>/', dm_olustur, name='dm_olustur'),
]