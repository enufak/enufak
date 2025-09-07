from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from enufak_mesaj.models import Mesaj, DM

@login_required
@csrf_exempt
@require_POST
def send_message(request, id):
    dm = get_object_or_404(DM, id=id)
    if request.user != dm.from_user and request.user != dm.to_user:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    data = json.loads(request.body)
    text = data.get('text', '').strip()
    if text:
        message = Mesaj.objects.create(dm=dm, sender=request.user, text=text)
        return JsonResponse({
            'id': message.id,
            'sender': message.sender.get_full_name(),
            'text': message.text,
            'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        })
    return JsonResponse({'error': 'Empty message'}, status=400)
