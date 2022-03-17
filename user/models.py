from django.db import models

# Create your models here.
class User_table(models.Model):
    nam=models.CharField(max_length=100)
    cnum=models.CharField(max_length=100)
    eml=models.CharField(max_length=100)
    gen=models.CharField(max_length=100)
    dep=models.CharField(max_length=100)
    password=models.CharField(max_length=100,default='website')
    uname=models.CharField(max_length=100)
   
    def __str__(self):
        return self.nam