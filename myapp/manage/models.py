from django.db import models


# Create your models here.
class Manage(models.Model):
    FIR_Number  = models.IntegerField(max_length=10)
    Item_Name = models.CharField(max_length=200)
    IPC_Section = models.CharField(max_length=200)
    Crime_scene = models.CharField(max_length=500)
    Crime_date = models.DateField()
    Crime_time = models.TimeField()
    Crime_witnesses = models.CharField(max_length=600)
    Crime_inspector = models.CharField(max_length=200)
    Item_status = models.BooleanField(default=True)
    where_its_kept = models.CharField(max_length=600)
    
    def __str__(self):
        return self.FIR_Number