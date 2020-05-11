from django.db import models

class Emp(models.Model):
    ename = models.CharField(max_length=100)
    salary = models.IntegerField()
class Student(Emp):
    sname = models.CharField(max_length=100)
    marks = models.IntegerField()
class Cust(Student):
    cname = models.CharField(max_length=100)
    sales = models.IntegerField()
