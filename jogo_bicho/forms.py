from django import forms

from jogo_bicho.models import JogoBicho

class JogoBichoForm(forms.ModelForm):

    class Meta:
        model = JogoBicho
        fields = ('bicho',)

        widgets = {
            'bicho': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Digite o nome...'}),
            
        }