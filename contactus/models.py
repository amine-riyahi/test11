from django.db import models
from django import forms 
from django.utils import timezone


class contactus(models.Model):
    fullname=models.CharField(max_length=30)
    msg=models.TextField()
    send_date=models.DateTimeField(timezone.now())
    email=models.TextField()
    
    


    
    def __str__(self):
        return self.fullname



