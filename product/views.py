from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import evry_product
from contactus.models import contactus
from  django.utils import timezone





# Create your views here.
def back (request):

    if request.method=='GET':



        
      
      
        objs=evry_product.objects.all()

        return render (request,'products/base.html',{'ez':'your message sent successfully','objs':objs})

def showpdf(request,bdfid):
    pdfonly = get_object_or_404(evry_product, pk=bdfid)
    return render(request,'products/pdf.html',{'pdfonly':pdfonly})

def productD(request,productD):
    proddetail = get_object_or_404(evry_product, pk=productD)
    return render(request,'products/proddetail.html',{proddetail:'proddetail'})







   




#def sendmail