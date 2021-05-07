from django.db import models

# Create your models here.


class Report(models.Model):
    year = models.CharField(max_length=100)
    petrolium_product = models.CharField(max_length=100)
    sales = models.IntegerField()
    country = models.CharField(max_length=100)
