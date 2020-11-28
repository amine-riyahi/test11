from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
     path('back',views.back,name='back' ),
  
    path('<int:bdfid>',views.showpdf,name='showpdf' ),
    path('<int:productD>',views.productD,name='productD' ),
]
