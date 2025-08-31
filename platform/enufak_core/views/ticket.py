from django.shortcuts import render, redirect
from enufak_core.forms import TicketForm
from enufak_core.models import Ticket
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def ticket_olustur(request):
    if request.method == "POST":
        if Ticket.objects.filter(yazar=request.user).exists():
            messages.error(request, "Zaten bir destek talebi açtınız. İşleme alınana kadar yeni talep açamazsınız.")
            return redirect("tickets")
        else:
            form = TicketForm(request.POST)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.yazar = request.user  
                ticket.save()
                return redirect("index")
    else:
        form = TicketForm()
    return render(request, "core/ticket.jinja", {"form": form})
