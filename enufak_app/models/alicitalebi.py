from django.db import models
from enufak_app.models import CustomUser


class AliciTalebi(models.Model):
    SURELER = (
        ('1','Gün içerisinde'),
        ('2','Birkaç gün içinde'),
        ('3','Bir hafta içinde'),
        ('4','Bir ay içinde'),
        ('5','Süre henüz belirtilmedi')
    )

    yazar = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    baslik = models.CharField(max_length=200)
    metin = models.TextField()
    süre = models.CharField(max_length=1, choices=SURELER)
    butce = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'alicitalebi'
        verbose_name = 'Alıcı Talebi'
        verbose_name_plural = 'Alıcı Talepleri'

    def __str__(self):
        return self.baslik