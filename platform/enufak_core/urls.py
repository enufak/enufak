from django.urls import path
from enufak_core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('ticket/', ticket_olustur, name='tickets'),
]