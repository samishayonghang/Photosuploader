from django import forms 
from.models import photohub,Authentic


class PhotohubForm(forms.ModelForm):
    class Meta:
        model= photohub
        fields='__all__'
        labels={'images':''}
    


class LoginForm(forms.ModelForm):
   class Meta:
      model= Authentic
      fields=['username','password']

class SignupForm(forms.ModelForm):
   class Meta:
      model= Authentic
      fields=['first_name','last_name', 'username','email','password']
class PhotohubForm(forms.ModelForm):
    class Meta:
        model = photohub
        exclude = ['user']  # Exclude the 'user' field


    