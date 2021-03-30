from django.db import models

# Create your models here.
class Employee(models.Model):
    fullName = models.CharField(max_length = 50,null=True)
    salary = models.IntegerField(null=True)
