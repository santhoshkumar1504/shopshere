from django import forms
from .models import AddressModel

class AddressForm(forms.ModelForm):           
    class Meta:
        model=AddressModel
        fields='__all__'
        exclude=['host']
      
