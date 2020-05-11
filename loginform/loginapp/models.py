from django.db import models

class InputFrm(models.Model):
    name = models.CharField(max_length=100)
