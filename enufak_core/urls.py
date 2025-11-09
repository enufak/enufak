from django.urls import path
from enufak_core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('ticket/', ticket_olustur, name='tickets'),
    path('sss/', sss, name='sss'),
    path('gizlilik/', gizlilik, name='gizlilik'),
    path('manifest.json', manifest, name='manifest'),
    path(".well-known/assetlinks.json", assetlinks, name="assetlinks"),
    path('kullanim-kosullari/', kullanim_kosullari, name='kullanim_kosullari'),
    path('indir/', indir, name='indir'),
    path('my-tickets/', my_tickets, name='my_tickets'),
    path('my-tickets/<int:id>/', ticket_detail, name='ticket_detail'),
    path('@<slug:slug>/', go_profile, name='go_profile'),
]