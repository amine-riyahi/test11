from django.db import models


class evry_product(models.Model):
    productname=models.CharField(max_length=30)
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
    bdf_file=models.FileField(upload_to='bdf/')
    


    def summary(self)  :


        return self.body[:28]+'...'  


    def __str__(self)  :


        return self.productname 
