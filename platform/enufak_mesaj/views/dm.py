from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from enufak_mesaj.models import DM

@login_required
def dm(request, id):
    dm = get_object_or_404(DM.objects.filter(
        id=id
    ).filter(
        Q(from_user=request.user) | Q(to_user=request.user)
    ))

    if request.user == dm.from_user:
        other_user = dm.to_user
    else:
        other_user = dm.from_user

    return render(request, 'mesaj/mesaj.jinja', {
        'dm': dm,
        'other_user':other_user,
    })
