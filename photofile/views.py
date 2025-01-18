from.models import photohub
from.forms import PhotohubForm,SignupForm,LoginForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from photofile.utils import send_activation_email

@login_required
def photos(request):
    images = photohub.objects.filter(user=request.user)
    if request.method=="POST":
        form=PhotohubForm(request.POST,request.FILES)
        if form.is_valid:

         photo=form.save(commit=False)
         photo.user=request.user
         photo.save()                    # Save the instance to the database
         messages.success(request, 'Photo uploaded successfully!')
         return redirect('home')
         



    else:
        form=PhotohubForm()
       
    return render(request,"photofile/photos.html",{'form':form,'images':images})

# def home(request):
#     return render(request,"photofile/base.html")

def register(request):
    if request.method=="POST":
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      username=request.POST.get('username')
      password=request.POST.get('password')
      email=request.POST.get('email')

      user=User.objects.filter(username=username)
      if user.exists():
         messages.info(request,'username already exists')
         return redirect('register')

      user=User.objects.create(
         first_name=first_name,
         last_name=last_name,
         username=username,
         password=password,
         email=email
      )
      user.set_password(password)
      user.save()
      uidb64=urlsafe_base64_encode(force_bytes(user.pk))
      token=default_token_generator.make_token(user)
      activation_link=reverse('activate',kwargs={'uidb64':uidb64,'token':token})
      activation_url=f'{settings.SITE_DOMAIN}{activation_link}'
      send_activation_email(user.email,activation_url)

      messages.info(request,'Account created Sucessfully')

      
      return redirect('loginpage')
      



    else:

     user=SignupForm()

    return render(request,'photofile/register.html',{'user':user})

    
def loginpage(request):
    form=LoginForm()
    if request.method=="POST":
     
      username=request.POST.get('username')
      password=request.POST.get('password')
      if not User.objects.filter(username=username).exists():
          messages.error(request,'Invalid Username')
          return redirect('loginpage')
      user=authenticate(username=username,password=password)
      if user is None:
          messages.error(request,'Invalid password')
          return redirect('loginpage')
      
          
          
      else:
         
         login(request,user)
         return redirect('home')
      
    return render(request,'photofile/loginpage.html',{'form':form})
   
    
def logoutpage(request):
   logout(request)
   return redirect('loginpage')

def activate_account(request,uidb64,token):
   try:
      uid=force_str(urlsafe_base64_decode(uidb64))
      user=User.objects.get(pk=uid)
      if user.is_active:
         messages.warning(request,"this account is alrady activated")
         return redirect('loginpage')
      if default_token_generator.check_token(user,token):
         user.is_active=True
         user.save()
         messages.success(request,"your account has been activated sucessfully")
         return redirect('loginpage')
      else:
         messages.error(request,"the activation link is invalid or has expired")
         return redirect('loginpage')
      

   except(TypeError,ValueError,OverflowError,User.DoesNotExist):
      messages.error(request,"invalid activation link")
      return redirect('loginpage')
   
      
   