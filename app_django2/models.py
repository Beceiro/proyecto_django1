from django.db import models

# Create your models here.

class Customer(models.Model):
    customer = models.CharField(("Clientes"), max_length=50)
    party_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField()