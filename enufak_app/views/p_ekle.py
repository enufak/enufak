from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from enufak_app.forms import PortfolyoForm
from django.contrib import messages

@login_required
def p_ekle(request):
    if request.method == "POST":
        form = PortfolyoForm(request.POST, request.FILES)
        if form.is_valid():
            portfolyo = form.save(commit=False)
            portfolyo.owner = request.user 
            portfolyo.save()
            messages.success(request, 'Portfolyonuz başarıyla eklendi.')
            return redirect("portfolyo")
    else:
        form = PortfolyoForm()

    return render(request, "app/p_ekle.jinja", {"form": form})