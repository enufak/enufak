from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from enufak_app.models import CustomUser
from enufak_mesaj.models import DM

@login_required
def dm_olustur(request, ids):
    ids = ids.split('-')
    from_user = get_object_or_404(CustomUser, id=int(ids[0]))
    to_user = get_object_or_404(CustomUser, id=int(ids[1]))

    if request.user != from_user:
        return redirect(request.META.get('HTTP_REFERER', '/'))

    mevcut_dm = DM.objects.filter(
        from_user=from_user,
        to_user=to_user
    ).first() or DM.objects.filter(
        from_user=to_user,
        to_user=from_user
    ).first()

    if mevcut_dm:
        return redirect('/mesajlar/')

    DM.objects.create(from_user=from_user, to_user=to_user)

    return redirect('/mesajlar/')
