from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enufak_app.models import Portfolyo


@login_required
def portfolyo(request):
    portfolyo = Portfolyo.objects.filter(owner=request.user).order_by('-id')

    return render(request, 'app/portfolyo.jinja', context={
        'portfolyo':portfolyo,
    })