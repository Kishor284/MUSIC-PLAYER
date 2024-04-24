from .models import signup
from django import forms

class Signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'