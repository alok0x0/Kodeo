from django.shortcuts import render
from .models import contact,product,recentproject,career,jobopening
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'kst/index.html')


def AboutUs(request):
    return render(request,'kst/aboutus.html')

def Services(request):
    return render(request,'kst/services.html')

def ContactUs(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        user=contact(name=name,email=email,phone=phone,subject=subject,message=message)
        user.save()
        messages.success(request,'Your Message Has Sent Succesfully')
    return render(request,'kst/contactus.html')

def Product(request):
    prod=product.objects.all()
    recent=recentproject.objects.all()
    # p=product.objects.filter('image')
    return render(request,'kst/product.html',{'prod':prod,'recent':recent})


def Career(request):
    opening=career.objects.all()
    return render(request,'kst/career.html',{'opening':opening})

def Jobapplication(request):
    opening = career.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        position=request.POST.get('position')
        date=request.POST.get('date')
        status=request.POST.get('status')
        resume=request.POST.get('resume')
        u=jobopening(name=name,email=email,phone=phone,position=position,date=date,status=status,resume=resume)
        u.save()
        messages.success(request,"Applied Successfully")
    return render(request,'kst/jobapplication.html',{'opening':opening})
