from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.

def home(request):
    # student_data = Student.objects.create(name='yesh',roll=104,city='Surat',marks='99',pass_date='2023-03-07')

    # student_data = Student.objects.filter(id=4).update(name='jay',marks='99')

    # student_data = Student.objects.update_or_create(id=4,name='jay',defaults={'name':'ROhit'})

    # student_data = Student.objects.latest('pass_date')

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

    # objs = [Student(name='ABC',roll='105',city='Srinagar',marks='56',pass_date='2021-08-09'),
    #         Student(name='DEF',roll='106',city='ganganagar',marks='45',pass_date='2021-12-05'),
    #         Student(name='GHI',roll='107',city='ganeshnagar',marks='76',pass_date='2023-11-04')]
    # student_data = Student.objects.bulk_create(objs)

#     all_student_data = Student.objects.all()

#     for std in all_student_data:
#         std.city='singapore'
#     student_data=Student.objects.bulk_update(all_student_data,['city'])

#     student_data = Student.objects.filter(marks='56').delete()

    # student_data = Student.objects.all().delete()

    # student_data = Student.objects.filter(name__exact='jay')

    # student_data = Student.objects.filter(pass_date__range=('2021-08-09','2023-08-01'))

    ##################### Q OBJECT #######################
    
    return render(request,'school/home.html',{'students':student_data})