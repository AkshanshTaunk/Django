from django.shortcuts import render
from .models import Student
from .forms import StudentRegistration

def studinfo(request):
    stud=Student.objects.get(pk=1)#query set ORM
    return render ( request,'enroll/studetails.html', {'std':stud} )
def showformdata(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
             print('from validated')
             print('Name:',fm.cleaned_data['name'])  
             print('Email:',fm.cleaned_data['email'])  
        else:
             fm=StudentRegistration()
    return render(request,'enroll/userregistration.html',{'form':fm}) 