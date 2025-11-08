from django.http import FileResponse, Http404
from django.conf import settings
import os

def serve_media(request, path):
    full_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(full_path):
        return FileResponse(open(full_path, 'rb'))
    raise Http404()
