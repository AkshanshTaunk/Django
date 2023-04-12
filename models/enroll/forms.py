from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError("Enter more than or equal to 4")
        valemail = self.cleaned_data['email']
        if len(valemail) < 10:
            raise forms.ValidationError("Enter more than or equal to 10")
    
   