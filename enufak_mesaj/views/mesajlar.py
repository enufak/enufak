from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from enufak_mesaj.models import DM, Mesaj
from django.shortcuts import get_object_or_404


@login_required
@require_GET
def dm_messages(request, id):
    dm = get_object_or_404(DM, id=id)
    if request.user != dm.from_user and request.user != dm.to_user:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    messages = dm.mesajlar.all()
    data = [
        {
            'id': m.id,
            'sender': m.sender.get_full_name(),
            'text': m.text,
            'created_at': m.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        } for m in messages
    ]
    return JsonResponse(data, safe=False)