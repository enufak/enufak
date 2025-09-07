from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from enufak_app.forms import GirisForm

def giris(request):
    if request.method == "POST":
        form = GirisForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["sifre"]
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect("app_index")
            else:
                form.add_error(None, "E-posta veya şifre yanlış.")
    else:
        form = GirisForm()
    return render(request, "app/giris.jinja", {"form": form})