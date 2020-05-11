from django.db import models

class Emp(models.Model):
    ename = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
class EmpProxy(Emp):
    class Meta:
        proxy = True

