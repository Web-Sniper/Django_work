from django.db import models as md

# Create your models here.
class Emp(md.Model):
    ename = md.CharField(max_length=100)
    email = md.EmailField(max_length=100)
    salary = md.IntegerField()
    location = md.CharField(max_length=100)
    def __tuple__(self):
        return self.ename
class Department(md.Model):
    dname = md.CharField(max_length=100)
    location = md.CharField(max_length=100)
