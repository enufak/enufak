from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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