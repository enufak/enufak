from django.db import models
from enufak_app.models import CustomUser

# Create your models here.
class DM(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='dm_gonderilen')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='dm_gelen')
    created_at = models.DateTimeField(auto_now_add=True)