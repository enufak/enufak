from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from enufak_app.models import Portfolyo
from django.contrib import messages


@login_required
def p_sil(request, id):
    p = get_object_or_404(Portfolyo, id=id)
    if p.owner == request.user:
        p.delete()
        messages.success(request, 'Portfolyo başarıyla kaldırıldı.')
        
        return redirect('portfolyo')
    else:
        return redirect('portfolyo')