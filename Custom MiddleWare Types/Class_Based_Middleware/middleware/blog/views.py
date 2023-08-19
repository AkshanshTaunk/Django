from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse 

# Create your views here.
def home(request):
    print("I am a view")
    return HttpResponse("This is Home page")

def exp(request):
    a = 10/0
    return HttpResponse("this is exception page")


def user_info(request):
    print("This is template user information")
    context = {'name':'jay'}
    return TemplateResponse(request,'blog/user.html',context)