from django.db import models

class CommanData(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    class Meta:
        abstract = True
class Emp(CommanData):
    salary = models.IntegerField()
class Student(CommanData):
    fee = models.IntegerField()
class Cust(CommanData):
    sales = models.IntegerField()