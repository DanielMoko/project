from django.db import models

# Create your models here.
class product(models.Model):
    productname = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    producttype = models.CharField(max_length=20)

