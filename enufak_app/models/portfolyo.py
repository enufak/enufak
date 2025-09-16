from django.db import models
from enufak_app.models import CustomUser


class Portfolyo(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    baslik = models.CharField(max_length=100)
    icerik = models.ImageField(upload_to='portfolios/')
    aciklama = models.TextField()
    link = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        db_table = 'portfolyo'
        verbose_name = 'Portfolyo'
        verbose_name_plural = 'Portfolyolar'


    def __str__(self):
        return self.baslik