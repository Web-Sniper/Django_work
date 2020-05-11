from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.sname
class Course(models.Model):
    student = models.OneToOneField(Student,on_delete=models.SET(4),null=True)
    cname = models.CharField(max_length=100)
    cfee = models.IntegerField()
    def __str__(self):
        return self.cname
