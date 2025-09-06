from django.urls import path
from enufak_mesaj.views import *


urlpatterns = [
    path('', mesajlarim, name='mesajlarim'),
    path('dm-olustur/<str:ids>/', dm_olustur, name='dm_olustur'),
    path('<int:id>/', dm, name='dm'),
    path('<int:id>/messages/', dm_messages, name='dm_messages'),
    path('<int:id>/send/', send_message, name='send_message'),
]