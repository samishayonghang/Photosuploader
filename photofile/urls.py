from django.urls import path

from.views import photos,loginpage,register

urlpatterns = [
    
    path('',photos,name='photos'),
    path('loginpage/',loginpage,name='loginpage'),
    path('register/',register,name='register'),
  
  
]
   
   
   
   

