from django.apps import AppConfig


class EnufakAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enufak_app'

    def ready(self):
        import enufak_app.signals