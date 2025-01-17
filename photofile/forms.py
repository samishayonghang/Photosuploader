from django import forms 
from.models import photohub


class PhotohubForm(forms.ModelForm):
    class Meta:
        model= photohub
        fields='__all__'
        labels={'images':''}
    


    

    