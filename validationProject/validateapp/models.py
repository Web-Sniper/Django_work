from django.db import models

class RegForm(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
