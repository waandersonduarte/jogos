from django import forms

from jogo_bicho.models import JogoBicho, Premio

class JogoBichoForm(forms.ModelForm):

    class Meta:
        model = JogoBicho
        fields = ('bicho',)
        

        widgets = {
            'bicho': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Digite o nome do animal...'}),
            
        }
class PremioForm(forms.ModelForm):
    class Meta:
        model = Premio
        fields = ('nome', 'telefone', 'email', 'endereco', 'tipo_aposta', 'num_conta')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome...'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu telefone...'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email...'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu endereço...'}),
            'tipo_aposta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu tipo de aposta...'}),
            'num_conta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu número...'}),
        }