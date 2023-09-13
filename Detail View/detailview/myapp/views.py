from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'myapp/student_list.html'
    # context_object_name = 'student'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'myapp/student_detail.html'
    # context_object_name = 'stu'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_student"] = self.model.objects.all().order_by('name')
        return context
    