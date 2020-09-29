from django.http import HttpResponse
from django.shortcuts import render,redirect
from photoapp.models import *

def show_about(request):
    name="Prakhar Site"
    link="https://www.google.com"
    data={
    'name':name,
    'link':link
    }
    return render(request,"about.html",data)
def show_home(request):
    categ=Category.objects.all()
    images=Image.objects.all()
    data={'images':images,'categ':categ}
    return render(request,"index.html",data)
def show_categ(request,cid):
    categ=Category.objects.all()
    category=Category.objects.get(pk=cid)
    images=Image.objects.filter(categ=category)
    data={'images':images,'categ':categ}
    return render(request,"index.html",data)

def home_page(request):
    return redirect('/home')
