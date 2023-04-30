from django.shortcuts import render,HttpResponseRedirect
from .forms import signupform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your sign up views here.
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

# Create your Login views here.
def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
         fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upassword = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upassword)
            if user is not None:
                login(request, user)
                messages.success(request,'Logged in successfully')
                return HttpResponseRedirect('/profile/')
        else:
         fm = AuthenticationForm()
        return render(request,'form/login.html',{'form':fm})
    else:
       return HttpResponseRedirect('/profile/')

# Create your /profile/ views here.
def user_profile(request):
    if request.user.is_authenticated:
     return render(request,'form/profile.html',{'name':request.user})
    else:
     return HttpResponseRedirect('/login/')

# Create your logout views here.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect ('/login/')