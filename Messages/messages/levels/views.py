from django.shortcuts import render
from .forms import StudentMesaage
from django.contrib import messages
# Create your views here.
def mess(request):
    if request.method=='POST':
        fm = StudentMesaage(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Your account has been created!!!')
            messages.add_message(request,messages.INFO,'Now you can login !!!')
            messages.add_message(request,messages.WARNING,'This is warning !')
            messages.add_message(request,messages.ERROR,'This is error !!!')
    else:
        fm = StudentMesaage()
    return render(request,'levels/message.html',{'form':fm})
