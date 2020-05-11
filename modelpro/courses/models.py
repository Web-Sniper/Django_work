from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    rollno = models.IntegerField()
    addr = models.CharField(max_length=100)

