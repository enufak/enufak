from django.urls import path
from enufak_proje.views import *


urlpatterns = [
    path('proje-olustur/<int:from_user>-<int:to_user>/', proje_olustur, name='proje_olustur'),
]