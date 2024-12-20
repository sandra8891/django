from django.db import models

# Create your models here.
class Gallery (models.Model):
    feedimage=models.ImageField(upload_to='image/')
