from django import forms
from signup.models import adddata
class formadddata(forms.ModelForm):
    class Meta():
        model=adddata
        fields = ['name','email','password']
