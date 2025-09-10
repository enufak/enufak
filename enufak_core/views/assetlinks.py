from django.http import JsonResponse

def assetlinks(request):
    data = [
        {
            "relation": ["delegate_permission/common.handle_all_urls"],
            "target": {
                "namespace": "android_app",
                "package_name": "com.enufak.twa",
                "sha256_cert_fingerprints": [
                    "67:81:E1:12:9C:70:D4:81:43:44:AD:27:C5:C8:65:9F:F0:E6:D3:E2:63:00:31:D5:4F:78:64:B3:FC:A6:28:6B"
                ]
            }
        }
    ]
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})
