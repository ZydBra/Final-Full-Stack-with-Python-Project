from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'prisijungimas', 'placeholder': 'Prisijungimo vardas...', 'required': 'required'}),
            'email': forms.TextInput(
                attrs={'class': 'prisijungimas', 'placeholder': 'Elektroninis paštas...', 'required': 'required'}),
            'first_name': forms.TextInput(
                attrs={'class': 'prisijungimas', 'placeholder': 'Įveskite savo vardą...'}),
            'last_name': forms.TextInput(
                attrs={'class': 'prisijungimas', 'placeholder': 'Įveskite savo pavardę...'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
            field.help_text = None
