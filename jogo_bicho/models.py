from xmlrpc.client import DateTime
from django.db import models
from django.utils import timezone

class JogoBicho(models.Model):
    bicho = models.CharField(max_length=200)
    #resultado_hora = models.DateTimeField(default=timezone.now, verbose_name='Data')

    def __str__(self):
        return self.bicho 