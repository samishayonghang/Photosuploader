from django.db import models

# Create your models here.
class photohub(models.Model):
    images=models.ImageField(upload_to="images")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded at {self.date}"
    
   





   


