from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

# class Home(TemplateView):
#     template_name='myapp/home.html'

class Home(TemplateView):
    template_name='myapp/home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='jay'
        context['rollNo']=101
        return context
