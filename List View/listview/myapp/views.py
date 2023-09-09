from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.

class StudentListView(ListView):
    model = Student
    # ordering = ['name']
    
    def get_queryset(self):
        return Student.objects.filter(course='C++')