from django.db import models
from enufak_app.models import CustomUser

class KullaniciYorumu(models.Model):
    yazan = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='yazan')
    yazilan = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='yazilan')
    yorum = models.TextField()
    puan = models.IntegerField()

    class Meta:
        db_table = 'kullanici_yorumu'
        verbose_name = 'Kullanıcı Yorumu'
        verbose_name_plural = 'Kullanıcı Yorumları'

    def __str__(self):
        return self.yorum