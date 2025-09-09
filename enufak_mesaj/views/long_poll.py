import time
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from enufak_mesaj.models import DM, Mesaj
from django.shortcuts import get_object_or_404

@login_required
def dm_messages_longpoll(request, id):
    dm = get_object_or_404(DM, id=id)
    if request.user != dm.from_user and request.user != dm.to_user:
        return JsonResponse({'error':'Unauthorized'}, status=403)
    
    last_id = int(request.GET.get('last_id', 0))
    timeout = 25
    interval = 0.5
    elapsed = 0

    while elapsed < timeout:
        new_messages = dm.mesajlar.filter(id__gt=last_id)
        if new_messages.exists():
            dm.mesajlar.filter(id__gt=last_id).exclude(sender=request.user).update(okunma=True)

            data = [
                {
                    'id': m.id,
                    'sender': m.sender.get_full_name(),
                    'text': m.text,
                    'created_at': m.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                } for m in new_messages
            ]
            return JsonResponse(data, safe=False)
        time.sleep(interval)
        elapsed += interval

    return JsonResponse([], safe=False)
