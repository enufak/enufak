from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

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