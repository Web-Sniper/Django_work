from django.db import models

class CurdOperations(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_id = models.IntegerField()
    prod_cost = models.IntegerField()
    prod_color = models.CharField(max_length=100)
    prod_weight = models.IntegerField()