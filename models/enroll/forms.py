from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5,max_length=15)
   