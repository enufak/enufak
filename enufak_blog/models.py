from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.
class Gonderi(models.Model):
    ETIKET = (
        ("1", "Haber"),
        ("2", "Güncelleme"),
        ('3', 'Duyuru'),
    )

    baslik = models.CharField(max_length=100)
    yazar = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    kapak_resmi = models.ImageField(upload_to='post_resimleri/', blank=True, null=True)  
    slug = AutoSlugField(populate_from='baslik', unique=True)
    etiket = models.CharField(max_length=1, choices=ETIKET)
    icerik = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'gonderi'
        verbose_name = 'Gönderi'
        verbose_name_plural = 'Gönderiler'

    def __str__(self):
        return self.baslik