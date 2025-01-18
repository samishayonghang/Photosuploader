from django.urls import path

from.views import photos,loginpage,register,logoutpage,activate_account

urlpatterns = [
    
    path('',photos,name='home'),
    path('loginpage/',loginpage,name='loginpage'),
    path('register/',register,name='register'),
    path('logout/',logoutpage,name='logout'),
    path('activate_account/<str:uidb64>/<str:token>/',activate_account,name='activate'),

    
  
  
]
   
   
   
   

