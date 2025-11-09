from django.shortcuts import redirect

def go_profile(request, slug):
    return redirect('kullanici', slug=slug)