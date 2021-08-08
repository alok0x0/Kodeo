from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import index,AboutUs,Services,ContactUs,Product,Career,Jobapplication

urlpatterns = [
    path('',index,name='home'),
    path('about',AboutUs,name='about'),
    path('services',Services,name='services'),
    path('contactus',ContactUs,name='contactus'),
    path('product',Product,name='product'),
    path('career',Career,name='career'),
    path('jobapplication',Jobapplication,name='jobapplication'),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)