from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from enufak_mesaj.models import DM
from django.db.models import Q

@login_required
def mesajlarim(request):
    dmler = DM.objects.filter(
        Q(from_user=request.user) | Q(to_user=request.user)
    ).select_related("from_user", "to_user").order_by("-created_at")

    return render(request, "mesaj/index.jinja", {"dmler": dmler})
