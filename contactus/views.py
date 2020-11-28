from django.shortcuts import render
from .models import contactus
from  django.utils import timezone
from product.models import evry_product



def create(request):

    if request.method=='POST':
        contactus_new=contactus()
        fullname=request.POST['Name']
        EmailOfTheClient=request.POST['Email']
        MsFrmClien=request.POST['Message']
        contactus_new.fullname=fullname
        contactus_new.send_date=timezone.now()
        contactus_new.msg=MsFrmClien
        contactus_new.email=EmailOfTheClient
        contactus_new.save()
        objs=evry_product.objects.all()

        return render (request,'products/base.html',{'ez':'your message sent successfully','objs':objs})
    else:
        if request.method=='GET':

            objs=evry_product.objects.all()
            return render (request,'products/base.html',{'objs':objs})
