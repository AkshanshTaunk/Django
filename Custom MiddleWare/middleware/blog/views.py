from django.shortcuts import HttpResponse 

# Create your views here.
def home(request):
    print("I am a view")
    return HttpResponse("This is Home page")