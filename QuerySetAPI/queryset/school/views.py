from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.

def home(request):
    student_data = Student.objects.get(marks='90')
    # student_data = Student.objects.order_by('?')           #randomly
    # student_data = Student.objects.order_by('-marks')     #desc order
    # student_data = Student.objects.order_by('city')   #asc order
    # student_data = Student.objects.exclude(marks=56)
    # student_data = Student.objects.filter(marks=90)
    # student_data = Student.objects.all()
    # student_data = Student.objects.order_by('id').reverse()[0:2] 
    # student_data = Student.objects.using('default')       #using(alias)   DATABASE
    ################# SECOND TABLE TEACHER ######################
    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # student_data = qs2.union(qs1)
    # print("Return:",student_data)
    # print("SQL Query:",student_data.query)
    return render(request,'school/home.html',{'students':student_data})