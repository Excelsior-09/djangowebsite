from django.db import models

# Create your models here.

class Record(models.Model):
    dt = models.CharField(max_length=15)
    odds = models.CharField(max_length=15)
    price = models.CharField(max_length=15)
