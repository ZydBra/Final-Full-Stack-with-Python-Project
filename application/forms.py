from django.forms import ModelForm
from .models import UzrasoKategorija, Uzrasas
from django import forms


class KategorijosForma(ModelForm):
    class Meta:
        model = UzrasoKategorija
        fields = ['kategorija']
        widgets = {
            'kategorija': forms.TextInput(
                attrs={'class': 'prisijungimas',
                       'placeholder': 'Įveskite kategorijos pavadinimą...',
                       'required': 'required'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
            field.help_text = None


class UzrasoForma(ModelForm):
    class Meta:
        model = Uzrasas
        fields = ['pavadinimas', 'uzrasas', 'uzraso_kategorija', 'nuotrauka']
        widgets = {
            'pavadinimas': forms.TextInput(
                attrs={'class': 'prisijungimas',
                       'placeholder': 'Užrašo pavadinimas...',
                       'required': 'required'}),
            'uzrasas': forms.Textarea(
                attrs={'class': 'prisijungimas',
                       'placeholder': 'Užrašo tekstas...',
                       'required': 'required'}),
            'uzraso_kategorija': forms.Select(
                attrs={'class': 'prisijungimas',
                       'label': 'Pasirikite kategoriją...',
                       'required': 'required'})
        }

    def __init__(self, *args, kategorijos_autorius=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['uzraso_kategorija'].queryset = UzrasoKategorija.objects.filter(
            kategorijos_autorius=kategorijos_autorius)

        for key, field in self.fields.items():
            field.help_text = None
