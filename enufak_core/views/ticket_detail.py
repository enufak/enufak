from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from enufak_core.models import Ticket


@login_required
def ticket_detail(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    if ticket.yazar == request.user:
        return render(request, 'core/ticket_detail.jinja', context={'ticket':ticket})
    else:
        return redirect('app_index')