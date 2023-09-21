from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Student
from .forms import StudentForm
from django.views.generic.base import TemplateView
# Create your views here.
class StudentCreateView(CreateView):
    form_class=StudentForm
    template_name='myapp/student_form.html'
    success_url = '/thanks/'

class ThanksTemplateView(TemplateView):
    template_name = 'myapp/thanks.html'

class StudentUpdateView(UpdateView):
    model=Student
    form_class=StudentForm
    template_name='myapp/student_form.html'
    success_url = '/thanksupdate/'

class UpdateTemplateView(TemplateView):
    template_name = 'myapp/update.html'

class StudentDeleteView(DeleteView):
    model = Student
    template_name='myapp/delete.html'
    success_url = '/create/'