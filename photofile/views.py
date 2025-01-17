from.models import photohub
from.forms import PhotohubForm
from django.shortcuts import render,redirect

def photos(request):
    images = photohub.objects.all()
    if request.method=="POST":
        form=PhotohubForm(request.POST,request.FILES)
        if form.is_valid:

         form.save()
         images = photohub.objects.all()
         



    else:
        form=PhotohubForm()
       
    return render(request,"photofile/photos.html",{'form':form,'images':images})

def home(request):
    return render(request,"photofile/base.html")

def loginpage(request):
    return render(request,"photofile/loginpage.html")

def register(request):
    return render(request,"photofile/register.html")

