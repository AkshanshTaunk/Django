from django.shortcuts import render,HttpResponse

# Create your views here.
# def home(request):
#     print("I am a view")
#     return HttpResponse("This is Home page")

def exp(request):
    a = 10/0
    return HttpResponse("this is exception page")