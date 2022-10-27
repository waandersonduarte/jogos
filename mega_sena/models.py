from django.db import models

class MegaSena(models.Model):
    num_1 = models.IntegerField()
    num_2 = models.IntegerField()
    num_3 = models.IntegerField()
    num_4 = models.IntegerField()
    num_5 = models.IntegerField()
    num_6 = models.IntegerField()

    def __str__(self):
        return self.num_1, self.num_2, self.num_3, self.num_4, self.num_5, self.num_6 
