from enufak_mesaj.models import Mesaj, DM

def unread_count(request):
    if request.user.is_authenticated:
        dmler = DM.objects.filter(from_user=request.user) | DM.objects.filter(to_user=request.user)
        unread_count = Mesaj.objects.filter(
            dm__in=dmler,
            okunma=False
        ).exclude(sender=request.user).count()
        return {"unread_count": unread_count}
    return {"unread_count": 0}
