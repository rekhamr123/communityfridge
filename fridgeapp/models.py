from django.db import models

# Create your models here.
class member(models.Model):
    membername=models.CharField(max_length=30)
    memberemail=models.EmailField()
    memberphone=models.CharField(max_length=12)
    memberpassword=models.CharField(max_length=20)
    booked_on=models.DateField(auto_now=True)

class donation(models.Model):
    membername=models.CharField(max_length=30)
    memberemail=models.EmailField()
    memberphone=models.CharField(max_length=12)
    memberaddress=models.CharField(max_length=50)
    donated_items=models.CharField(max_length=100)
    donation_date=models.DateField(auto_now=True)

class admin_items(models.Model):
    admin_name = models.CharField(max_length=50)
    item1=models.CharField(max_length=50)
    item2=models.CharField(max_length=50)
    item3=models.CharField(max_length=50)
    item4=models.CharField(max_length=50)
    item5=models.CharField(max_length=50)
    item6=models.CharField(max_length=50)
    item7=models.CharField(max_length=50)
    item8=models.CharField(max_length=50)
    item9=models.CharField(max_length=50)
    submit_on = models.DateField(auto_now=True)

class requesteditems(models.Model):
    requester_name=models.CharField(max_length=30)
    requester_email=models.EmailField()
    requester_phone=models.CharField(max_length=12)
    requester_address=models.CharField(max_length=50)
    request_items=models.CharField(max_length=300)
    request_date=models.DateField(auto_now=True)


