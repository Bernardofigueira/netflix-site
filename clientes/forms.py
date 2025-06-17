from django import forms #Importar o forms
from .models import Cliente #Importa o modelo (ex: Cliente)
from django.core.exceptions import ValidationError
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente #Modelo (Classe do model)
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'data_nascimento',
            'telefone',
            'email',
            'senha'
        ]

        #Opcional - Personlização do input do formulario
        widgets = {
        'nome': forms.TextInput(attrs={"class": "form-control input", "placeholder": "Digite seu nome"}),
        'sobrenome': forms.TextInput(attrs={"class": "form-control input", "placeholder": "Digite seu sobrenome"}),
        'cpf': forms.TextInput(attrs={"class": "form-control input", "placeholder": "___ . ___ . ___ - __"}),
        'data_nascimento': forms.DateInput(attrs={"class": "form-control input", "placeholder": "DD/MM/AAAA", "type": "date"}),
        'telefone': forms.TextInput(attrs={"class": "form-control input", "placeholder": "(XX) XXXX-XXXX"}),
        'email': forms.EmailInput(attrs={"class": "form-control input", "placeholder": "email@example.com"}),
        'senha': forms.TextInput(attrs={"class": "form-control input", "placeholder": "Digite sua senha", "type": "password"}),
        }
        
