from django.db import models

# Create your models here.
class Listitime(models.Model):
    name1=models.CharField(max_length=100)
    date1=models.CharField(max_length=100)
    course1=models.CharField(max_length=100)

