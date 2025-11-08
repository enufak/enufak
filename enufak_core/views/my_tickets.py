from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from enufak_core.models import Ticket

@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(yazar=request.user).order_by('-created_at')
    
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    
    if search_query:
        tickets = tickets.filter(
            Q(baslik__icontains=search_query) | 
            Q(konu__icontains=search_query)
        )
    
    if status_filter == 'open':
        tickets = tickets.filter(is_active=True)
    elif status_filter == 'closed':
        tickets = tickets.filter(is_active=False)
    
    context = {
        'tickets': tickets,
    }
    return render(request, 'core/my_tickets.jinja', context=context)