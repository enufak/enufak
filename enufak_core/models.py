from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Ticket(models.Model):
    TICKET_TURU = (
        ('0', 'Kimlik Doğrulaması'),
        ("1", "Teknik Problem"),
        ("2", "Kullanıcı Bildirimi"),
        ('3', 'Ekip'),
        ('4', 'Onaylı Kullanıcı'),
    )

    tur = models.CharField(max_length=1, choices=TICKET_TURU)
    baslik = models.CharField(max_length=200)
    resim = models.ImageField(upload_to='destek/', blank=True, null=True)
    konu = models.TextField()
    yazar = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    yetkili_mesaj = models.TextField(blank=True, null=True)


    class Meta:
        db_table = 'ticket'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Ticketlar'

    def __str__(self):
        return self.baslik