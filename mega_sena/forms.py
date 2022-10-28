from django import forms
from mega_sena.models import MegaSena

class MegaSenaForm(forms.ModelForm):

    class Meta:
        model = MegaSena
        fields = ('num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6',)

        widgets = {
            'num_1': forms.TextInput(attrs={ 'class': 'form-control'}),
            'num_2': forms.TextInput(attrs={ 'class': 'form-control'}),
            'num_3': forms.TextInput(attrs={ 'class': 'form-control'}),
            'num_4': forms.TextInput(attrs={ 'class': 'form-control'}),
            'num_5': forms.TextInput(attrs={ 'class': 'form-control'}),
            'num_6': forms.TextInput(attrs={ 'class': 'form-control'}),
            
        }