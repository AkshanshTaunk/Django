from django.shortcuts import render
from .models import Student,ProxyStudent
# Create your views here.

def home(request):
    # student_data=Student.objects.all()
    student_data=ProxyStudent.students.get_stu_roll_range(1,2)
    return render(request,'student/home.html',{'student':student_data})