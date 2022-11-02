from tabnanny import verbose
from xmlrpc.client import DateTime
from django.db import models
from django.utils import timezone

class JogoBicho(models.Model):
    bicho = models.CharField(max_length=200, verbose_name='Nome do Bicho:')
    #resultado_hora = models.DateTimeField(default=timezone.now, verbose_name='Data')

    def __str__(self):
        return self.bicho 

class Premio(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome:')
    telefone = models.CharField(max_length=200, verbose_name='Telefone:')
    email = models.CharField(max_length=200, verbose_name='E-mail:')
    endereco = models.CharField(max_length=200, verbose_name='Endereço:')
    tipo_aposta = models.CharField(max_length=200, verbose_name='Tipo de aposta:')
    num_conta = models.CharField(max_length=200, verbose_name='Número da Conta:')
    
    def __str__(self):
        return self.nome 