from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Project

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from django.contrib.auth import get_user_model
from django.utils import timezone
from enufak_mesaj.models import Mesaj, DM
import hashlib
from enufak_app.models import CustomUser
import base64
from django.db import models


def encode_room_id(project_id, secret_key):
    data = f"{project_id}{secret_key}".encode()
    hashed = hashlib.sha256(data).digest()
    token = base64.urlsafe_b64encode(hashed).decode()[:16]
    return token

User = get_user_model()


@login_required
def start_or_go_video_call(request, to_user_id):
    from_user = request.user
    to_user = get_object_or_404(CustomUser, id=to_user_id)

    dm_qs = DM.objects.filter(
        models.Q(from_user=min(from_user, to_user, key=lambda u: u.id), 
                to_user=max(from_user, to_user, key=lambda u: u.id)) |
        models.Q(from_user=max(from_user, to_user, key=lambda u: u.id),
                to_user=min(from_user, to_user, key=lambda u: u.id))
    )
    if dm_qs.exists():
        dm = dm_qs.first()
    else:
        dm = DM.objects.create(
            from_user=min(from_user, to_user, key=lambda u: u.id),
            to_user=max(from_user, to_user, key=lambda u: u.id)
        )

    Mesaj.objects.create(
        dm=dm,
        sender=request.user,
        text="Görüntülü sohbet başlatıldı!",
        created_at=timezone.now()
    )

    project_qs = Project.objects.filter(
        customer=min(from_user, to_user, key=lambda u: u.id),
        freelancer=max(from_user, to_user, key=lambda u: u.id)
    )
    if project_qs.exists():
        project = project_qs.first()
    else:
        project = Project.objects.create(
            title=f"{from_user.get_full_name} - {to_user.get_full_name} Sohbet",
            customer=min(from_user, to_user, key=lambda u: u.id),
            freelancer=max(from_user, to_user, key=lambda u: u.id)
        )

    return redirect('video_call_jitsi', project_id=project.id)


@login_required
def video_call(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.user != project.customer and request.user != project.freelancer:
        return HttpResponseForbidden("Bu projeye erişim yetkiniz yok.")

    def encode_room_id(project_id, secret_key):
        data = f"{project_id}{secret_key}".encode()
        hashed = hashlib.sha256(data).digest()
        token = base64.urlsafe_b64encode(hashed).decode()[:16]
        return token

    room_name = f"room_{encode_room_id(project.id, settings.SECRET_KEY)}"
    jitsi_server = "https://jitsi.riot.im"
    redirect_url = request.META.get('HTTP_REFERER', '/')

    return render(request, "video/video.jinja", {
        "room_name": room_name,
        "username": request.user.get_full_name(),
        "jitsi_server": jitsi_server,
        "redirect_url": redirect_url
    })
