# Geliştirici Ortamının Kurulması

_**Lazım Olanlar:** Python 3.12, Pipenv_

> Python 3.12'yi python.org sayfasından indirebilirsiniz.


## Environment Kurulumu
```bash
pip install pipenv
```

ardından `platform` klasörü içinde komut satırı açıp,
```bash
pipenv install
```

```bash
pipenv shell
```

## Veritabanı Migrasyonu
Sanal ortamımızı ve modüllerimizi kurduk. şimdi yapmamız gereken veritabanını migrate etmek.

```bash
python manage.py migrate
```

### Superuser oluşturma
eğer testleri yapabilmek için bi root kullanıcı eklemek isterseniz migrate ettikten sonra `python manage.py createsuperuser` komutunu kullanın.


## Sunucuyu Başlatma
Gerekli işlemlerimizi yaptık. Şimdi sunucuyu ayağa kaldıralım.

Komut satırında şu komutu çalıştırın;
```bash
python manage.py runserver
```

ve işlem tamam.

`http://localhost:8000` adresinden sayfaya ulaşabilirsiniz.


### Frontend Düzenlemeleri
Django altyapısı ile beraber jinja şablon motorunu kullanıyoruz. platform altındaki templates dizini içerisinden şablonları düzenleyebilirsiniz.
