from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(label='Password:',widget=forms.PasswordInput)
   
    
    