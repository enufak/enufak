from django.db import models
from enufak_app.models import CustomUser


# Create your models here.
class Proje(models.Model):
    SURELER = (
        ('1','Gün içerisinde'),
        ('2','Birkaç gün içinde'),
        ('3','Bir hafta içinde'),
        ('4','Bir ay içinde'),
        ('5','Süre henüz belirtilmedi')
    )

    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='olusturan')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='gonderilen')

    baslik = models.CharField(max_length=150)
    konu = models.TextField()
    sure = models.CharField(max_length=1, choices=SURELER)
    ucret = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'projeler'
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'

    def __str__(self):
        return self.konu