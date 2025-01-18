from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class photohub(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    images=models.ImageField(upload_to="images")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded at {self.date}"
    
   
class Authentic(models.Model):
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100, unique=True)
    first_name=models.CharField(verbose_name='First Name',max_length=100,default='Alice')
    last_name=models.CharField(verbose_name='Last Name',max_length=100,default="carter")
    is_active = models.BooleanField(default=False)




   


