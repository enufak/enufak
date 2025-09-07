from django.shortcuts import render, get_object_or_404
from enufak_blog.models import Gonderi

# Create your views here.
def index(request):
    gonderiler = Gonderi.objects.all().order_by('-id')
    return render(request, 'blog/index.jinja', context={
        'gonderiler':gonderiler,
    })

def post_detail(request, slug):
    gonderi = get_object_or_404(Gonderi, slug=slug)
    return render(request, 'blog/detay.jinja', context={
        'gonderi':gonderi,
    })