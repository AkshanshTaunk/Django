from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    student_data = Student.objects.exclude(marks=56)
    # student_data = Student.objects.filter(marks=90)
    # student_data = Student.objects.all()
    print("Return:",student_data)
    print("SQL Query:",student_data.query)
    return render(request,'school/home.html',{'students':student_data})