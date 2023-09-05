from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class MyView(View):
    name='Akshansh'
    def get(self,request):
        return HttpResponse(self.name)

class MyViewChild(MyView):
    def get(self):
        return HttpResponse(self.name)