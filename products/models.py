from django.db import models

# Create your models here.
class products_model(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.IntegerField()


    def __str__(self):
        return self.name