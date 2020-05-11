from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)