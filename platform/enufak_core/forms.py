from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['tur', 'baslik', 'konu']
        widgets = {
            'tur': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-400 focus:outline-none',
            }),
            'baslik': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-400 focus:outline-none',
                'placeholder': 'Başlık giriniz'
            }),
            'konu': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-400 focus:outline-none',
            }),
        }