from django.shortcuts import render
from .forms import signupform
from django.contrib import messages
# Create your views here.
def sign_up(request):
    if request.method =="POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created successfully in dbsql-lite')
            messages.info(request,'Username already existed')
            fm.save()
    else:
        fm = signupform()
    return render (request,'form/sign_up.html',{'form':fm})