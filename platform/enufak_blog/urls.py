from django.urls import path
from enufak_blog.views import *

urlpatterns = [
    path('', index),
    path('<slug:slug>/', post_detail),
]