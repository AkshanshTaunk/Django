from django.shortcuts import render
from .models import User
from .forms import StudentRegistration

def home(request):
    return render(request,'enroll/home.html')

def showformdata(request,my_id):
    if my_id == 1:
        student = {'id':my_id,'name':'Rohan'}
    if my_id == 2:
        student = {'id':my_id,'name':'jay'}
    if my_id == 3:
        student = {'id':my_id,'name':'veer'}    
    return render(request,'enroll/userregistration.html', student)