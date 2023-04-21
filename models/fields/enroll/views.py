from django.shortcuts import render
from .forms import StudentRegistration

def showformfields(request):
    fm =  StudentRegistration()
    return render(request,'enroll/userfields.html',{'form':fm})