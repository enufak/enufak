from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from enufak_app.models import *

User = get_user_model()



class KayitForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="E-posta",
        help_text="Lütfen aktif olarak kullandığınız bir e-posta adresi giriniz.",
        widget=forms.EmailInput(attrs={"placeholder": "E-posta adresinizi girin"})
    )
    first_name = forms.CharField(
        required=True,
        label="Ad",
        widget=forms.TextInput(attrs={"placeholder": "Adınızı girin"})
    )
    last_name = forms.CharField(
        required=True,
        label="Soyad",
        widget=forms.TextInput(attrs={"placeholder": "Soyadınızı girin"})
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu e-posta zaten kayıtlı.")
        return email

class GirisForm(forms.Form):
    email = forms.EmailField(label="E-posta", widget=forms.EmailInput(attrs={"placeholder": "E-posta"}))
    sifre = forms.CharField(label="Şifre", widget=forms.PasswordInput(attrs={"placeholder": "Şifre"}))


class ProfilDuzenleForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "konum", "biyografi", "avatar")
        labels = {
            "first_name": "Ad",
            "last_name": "Soyad",
            "email": "E-posta",
            "konum": "Konum",
            "biyografi": "Biyografi",
            "avatar": "Profil Fotoğrafı",
        }
        help_texts = {
            "first_name": "Adınızı giriniz.",
            "last_name": "Soyadınızı giriniz.",
            "email": "Geçerli bir e-posta adresi yazınız.",
            "konum": "Bulunduğunuz şehir veya ülkeyi yazabilirsiniz.",
            "biyografi": "Kendinizi kısaca tanıtın (max 300 karakter).",
            "avatar": "Profil fotoğrafınızı yükleyin (opsiyonel).",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("first_name"),
            Field("last_name"),
            Field("email"),
            Field("konum"),
            Field("biyografi"),
            Field("avatar", css_class="file-input bg-white border border-gray-300 rounded-lg p-2")
        )

        if "password" in self.fields:
            self.fields.pop("password")

        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({
                    "class": "block w-full text-sm text-gray-500 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "block w-full rounded-lg border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                    "rows": "4",
                    "placeholder": "Kendinizi kısaca tanıtın..."
                })
            else:
                field.widget.attrs.update({
                    "class": "block w-full rounded-lg border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                    "placeholder": field.label
                })


class IlanEkleForm(forms.ModelForm):
    class Meta:
        model = Ilan
        fields = ["ilan_baslik", "ilan_metni", "konum", "is_deneyimi",'istenilen_ucret','etiketler']
        labels = {
            "ilan_baslik": "İlan Başlığı",
            "ilan_metni": "İlan Açıklaması",
            "konum": "Konum",
            "is_deneyimi": "İş Deneyimi",
            'istenilen_ucret': 'İstenilen Ücret (₺)',
            'etiketler':'Etiketler'
        }
        widgets = {
            "ilan_baslik": forms.TextInput(attrs={
                "class": "block w-full rounded-lg border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                "placeholder": "Örn: Web sitesi tasarımı"
            }),
            "ilan_metni": forms.Textarea(attrs={
                "class": "block w-full rounded-lg border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                "rows": 5,
                "placeholder": "İlan ile ilgili detayları buraya yazın..."
            }),
            "konum": forms.TextInput(attrs={
                "class": "block w-full rounded-lg border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                "placeholder": "Örn: İstanbul"
            }),
            "is_deneyimi": forms.Textarea(attrs={
                "class": "block w-full rounded-lg border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                "rows": 3,
                "placeholder": "İş tecrübelerinizi yazın..."
            }),
            "istenilen_ucret": forms.NumberInput(attrs={
                "class": "block w-full rounded-lg border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                "placeholder": "Örn: 2500",
                "min": "0",
            }),
            "etiketler": forms.Textarea(attrs={
                "class": "block w-full rounded-lg border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                "rows": 2,
                "placeholder": "Örnek: bahçe elektronik yazılım sanayi tesisat"
            }),
        }
        help_texts = {
            'etiketler': 'Lütfen etiket kelimeleri sadece kelime olacak şekilde ayrı ayrı yazınız.',
        }


class AliciTalebiForm(forms.ModelForm):
    class Meta:
        model = AliciTalebi
        fields = ['baslik', 'metin', 'süre', 'butce']
        labels = {
            'baslik': 'Talep Başlığı',
            'metin': 'Talep Detayları',
            'süre': 'İstenilen Süre',
            'butce': 'Bütçe (₺)',
        }
        widgets = {
            'baslik': forms.TextInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 shadow-sm focus:ring-yellow-500 focus:border-yellow-500 p-3',
                'placeholder': 'Talebin başlığını girin'
            }),
            'metin': forms.Textarea(attrs={
                'class': 'block w-full rounded-lg border-gray-300 shadow-sm focus:ring-yellow-500 focus:border-yellow-500 p-3',
                'placeholder': 'Talebin detaylarını buraya yazın',
                'rows': 5
            }),
            'süre': forms.Select(attrs={
                'class': 'block w-full rounded-lg border-gray-300 shadow-sm focus:ring-yellow-500 focus:border-yellow-500 p-3'
            }),
            'butce': forms.NumberInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 shadow-sm focus:ring-yellow-500 focus:border-yellow-500 p-3',
                'placeholder': 'Bütçenizi girin (₺)'
            }),
        }