from django.db import models
from enufak_app.models import CustomUser

# Create your models here.
class DM(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='dm_gonderilen')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='dm_gelen')

    created_at = models.DateTimeField(auto_now_add=True)


class Mesaj(models.Model):
    dm = models.ForeignKey(DM, on_delete=models.CASCADE, related_name='mesajlar')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.sender.username}: {self.text[:20]}'