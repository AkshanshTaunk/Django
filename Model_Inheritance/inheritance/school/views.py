from django.shortcuts import render
from .models import Student,Teacher, Contractor
# Create your views here.

def home(request):
    student_data=Student.objects.all()
    teacher_data=Teacher.objects.all()
    contractor_data=Contractor.objects.all()
    return render(request,'school/home.html',{'student':student_data,'teacher':teacher_data,'contractor':contractor_data})
 