from django.db import models

# Create your models here.
class student(models.Model):
    name =  models.CharField(max_length=200)
    collage = models.CharField(max_length=200)
    age = models.IntegerField(max_length=10)
    is_Active = models.BooleanField(default=False)