from django import forms
from mega_sena.models import MegaSena

class MegaSenaForm(forms.ModelForm):

    class Meta:
        model = MegaSena
        fields = ('num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6',)

        widgets = {
            'num_1': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Digite o número 01...'}),
            'num_2': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Digite o número 02...'}),
            'num_3': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Digite o número 03...'}),
            'num_4': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Digite o número 04...'}),
            'num_5': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Digite o número 05...'}),
            'num_6': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Digite o número 06...'}),
            
        }