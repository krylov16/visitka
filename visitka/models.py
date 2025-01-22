from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=150)

class Questoins(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.CharField(max_length=150)


