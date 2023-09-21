from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from .models import Student
from django.views.generic.base import TemplateView
# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','password']
    success_url = '/thanks/'

class ThanksTemplateView(TemplateView):
    template_name = 'myapp/thanks.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','password']
    success_url = '/thanksupdate/'


class UpdateTemplateView(TemplateView):
    template_name = 'myapp/update.html'