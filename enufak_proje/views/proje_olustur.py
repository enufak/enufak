from django.shortcuts import redirect
from enufak_proje.models import Proje
from django.contrib.auth.decorators import login_required


@login_required
def proje_olustur(request, from_user, to_user):
    if from_user == request.user or to_user == request.user:
        pass

        #TODO: Buraya, frontendden gönderilen proje oluştur form dataları çekilerek
        #      proje modelinde bir obje oluşturan ve gerekli filtrelemeleri yapan bir
        #      view yazılacak.
    else:
        return redirect('mesajlarim')