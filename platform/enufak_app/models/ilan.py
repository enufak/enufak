from django.db import models
from enufak_app.models import CustomUser


class Ilan(models.Model):
    ilan_sahibi = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    ilan_baslik = models.CharField(max_length=150)
    ilan_metni = models.TextField(max_length=1000)
    konum = models.CharField(max_length=25, blank=True, null=True)
    is_deneyimi = models.TextField()
    istenilen_ucret = models.IntegerField()
    etiketler = models.CharField(max_length=100, blank=True, null=True)
    aktif = models.BooleanField(default=False)

    class Meta:
        db_table = 'ilan'
        verbose_name = 'İlan'
        verbose_name_plural = 'İlanlar'

    def __str__(self):
        return self.ilan_baslik