from multiprocessing import context
from django.shortcuts import render , HttpResponse
from .models import product ,Contact, Resume
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
# Create your views here.

def home(request):
    bio = Resume.objects.all()
    context = {'bio': bio}
    return render(request,'home.html',context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact=Contact(name=name, desc=desc, email=email,phone=phone ,date= datetime.now())
        contact.save()
        messages.success(request, "Your message has been sent !") 
    return render(request,'contact.html')

def categoryView(request):
        category = product.objects.all().order_by('Date')
        return render(request, 'categories.html', {'category': category})


def product_detail(request,pk=None):
    prod = product.objects.get(pk=pk)
    return render(request, 'product.html', { 'prod': prod})

