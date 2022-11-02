from django.db import models

class MegaSena(models.Model):
    num_1 = models.IntegerField(verbose_name='Número 01:')
    num_2 = models.IntegerField(verbose_name='Número 02:')
    num_3 = models.IntegerField(verbose_name='Número 03:')
    num_4 = models.IntegerField(verbose_name='Número 04:')
    num_5 = models.IntegerField(verbose_name='Número 05:')
    num_6 = models.IntegerField(verbose_name='Número 06:')

    def __str__(self):
        return self.num_1, self.num_2, self.num_3, self.num_4, self.num_5, self.num_6 
