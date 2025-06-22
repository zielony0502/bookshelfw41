from django.db import models

class  Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
