from django.http import JsonResponse

def manifest(request):
    return JsonResponse({
        "name": "EnUfak",
        "short_name": "EnUfak",
        "start_url": "/uygulama/kesfet/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#facc15",
        "scope": "/",
        "icons": [
            {
                "src": "/assets/images/logo.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "/assets/images/logo.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    })
