from django.db import models
from django.contrib.auth.models import User

# from django.db import forms

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class product(models.Model):
    title=models.CharField(max_length=500)
    decs=models.CharField(max_length=500)
    image=models.ImageField(upload_to='image')

class recentproject(models.Model):
    image=models.ImageField(upload_to='Upload_Recent_Project')

class career(models.Model):
    title=models.CharField(max_length=500)
    decs=models.CharField(max_length=500)
# status_choices=(
#     ('student','STUDENT'),
#     ('employee','EMPLOYEE'),
#     ('selfemployee','SELFEMPLOYEE'),
#     ('unemployee','UNEMPLOYEE'),
# )
class jobopening(models.Model):
    name=models.CharField(max_length=500)
    email=models.EmailField(max_length=500)
    phone=models.CharField(max_length=500)
    position=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=500)
    resume=models.FileField(upload_to=None,max_length=500)

    def __str__(self):
        return self.name
