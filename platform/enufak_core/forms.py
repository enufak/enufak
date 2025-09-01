from django import forms
from .models import Ticket
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column("tur", css_class="sm:col-span-3"),
                Column("baslik", css_class="sm:col-span-3"),
                css_class="grid grid-cols-1 sm:grid-cols-6 gap-x-6 gap-y-8"
            ),
            Row(
                Column("konu", css_class="sm:col-span-6"),
            ),
            Submit("submit", "Gönder", css_class="rounded-md bg-yellow-400 px-3 py-2 text-sm font-semibold text-white hover:bg-yellow-500 focus:ring-2 focus:ring-indigo-600")
        )