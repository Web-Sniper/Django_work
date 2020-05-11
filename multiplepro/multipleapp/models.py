from django.db import models

class Emp(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100)
    salary = models.IntegerField()
class Cust(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)
    sales = models.IntegerField()
class Student(Emp,Cust):
    sname = models.CharField(max_length=100)
    marks = models.IntegerField()
