from django import forms
from .models import User

class StudentMesaage(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'