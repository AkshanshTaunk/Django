from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # student_data=Student.objects.all()
    student_data=Student.students.all()
    return render(request,'student/home.html',{'student':student_data})