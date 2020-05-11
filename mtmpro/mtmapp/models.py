from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.sname
class Course(models.Model):
    student = models.ManyToManyField(Student)
    cname = models.CharField(max_length=100)
    cfee = models.IntegerField()
    def __str__(self):
        return self.cname
