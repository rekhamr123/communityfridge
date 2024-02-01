from django.contrib import messages
from django.shortcuts import render,redirect
from . models import member,donation,admin_items,requesteditems
from datetime import date
from django.contrib.auth.models import auth

from django.conf import settings

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def donations(request):
    if request.method == 'POST':
        username = request.POST["name"]
        email = request.POST["email"]
        phone=request.POST["phone"]
        address = request.POST["address"]
        item = request.POST.getlist("items")
        donation(membername=username,memberemail=email,memberphone=phone,memberaddress=address,donated_items=item).save()
        messages.success(request, "Donated successfully,Thank you.")
        return redirect('/')
    return render(request, 'index.html')

def item_request(request):
    today = date.today()
    items = {
        'item': admin_items.objects.filter(submit_on=today)
    }
    if items:
        return render(request, "request.html", items)
    else:
        messages.info(request,"Sorry,Today There is no Items in the fridge")
        return render(request, "request.html")



def requests(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST.get("email")
        phone=request.POST.get("phone")
        address = request.POST.get("address")
        item = request.POST.getlist('items')
        saved=requesteditems(requester_name=username,requester_email=email,requester_phone=phone,requester_address=address,request_items=item).save()
        if saved:
            messages.info(request,"Requested successfully")
            return redirect('/')
    return render(request, 'index.html')


def memberregistration(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone=request.POST.get("phone")
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password==cpassword:
            if member.objects.filter(membername=username).exists():
                messages.info(request,"Username Exists")
                return redirect("http://127.0.0.1:8000/memberregistration/")
            elif member.objects.filter(memberemail=email).exists():
                messages.info(request,"Email Exists")
                return redirect("http://127.0.0.1:8000/memberregistration/")
            else:
                saved=member(membername=username,memberemail=email,memberphone=phone,memberpassword=password).save()
                if saved:
                    messages.info(request,"Registration success")
                return redirect('http://127.0.0.1:8000/memberlogin/')
        else:
            messages.info(request,"Confirm password Not matched")
            return redirect("http://127.0.0.1:8000/memberregistration/")
    return render(request, 'memberregistration.html')

def memberlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        members=member.objects.filter(memberemail=email,memberpassword=password)
        if members:
            member_detail={'user': member.objects.filter(memberemail=email,memberpassword=password)}
            return render(request,'donation.html',member_detail)
        else:
            messages.info(request,"Not registered")
    return render(request,'memberlogin.html')

def donatedlist(request):
    today=date.today()
    items = {
        'item': donation.objects.filter(donation_date=today)
    }
    if items:
        return render(request, "donated_items.html", items)
    else:
        messages.info(request,"Sorry,Today There is no Items in the fridge")
        return render(request, "donated_items.html")

def requestedlist(request):
    today=date.today()
    ritems = {
        'requestitem': requesteditems.objects.filter(request_date=today)
    }
    if ritems:
        return render(request, "requested_items.html", ritems)
    else:
        messages.info(request,"Sorry,Today There is no Requests")
        return render(request, "requested_items.html")

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("admin/")
        else:
            messages.info(request,"Not registered")
            return redirect("http://127.0.0.1:8000/login/")
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def admin(request):
        return render(request, 'admin.html')

