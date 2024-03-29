from django.shortcuts import render,HttpResponseRedirect
from .forms import signupform, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.models import User
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

# Create your /profile/ views here.
def user_profile(request):
    if request.user.is_authenticated:
     if request.method=="POST":
        if request.user.is_superuser == True:
            fm = EditAdminProfileForm(request.POST,instance=request.user)
            users = User.objects.all()
        else:
            fm = EditUserProfileForm(request.POST, instance=request.user)
            users = None
        if fm.is_valid():
            messages.success(request,'Profile Upadted Successfully')
            fm.save()
     else:
       if request.user.is_superuser == True:
          fm = EditAdminProfileForm(instance=request.user)
          users = User.objects.all()
       else:
          fm = EditUserProfileForm(instance=request.user) 
          users = None
     return render(request,'form/profile.html',{'name':request.user.username,'form':fm,'users':users})
    else:
     return HttpResponseRedirect('/login/')

# Create your logout views here.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect ('/login/')

# Create your logout views here.
def user_pass_change(request):
    if request.user.is_authenticated:
      if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)    
            messages.success(request,'password changed successfully')
            return HttpResponseRedirect('/profile/')
      else:     
        fm = PasswordChangeForm(user=request.user)
        return render(request,'form/changepass.html', {'form':fm})
    else:
       return HttpResponseRedirect('/login/')
    
# Create your user detail here.
def user_detail(request,id):
   if request.user.is_authenticated:
      pi = User.objects.get(pk=id)
      fm = EditAdminProfileForm(instance=pi)
      return render(request,'form/userdetail.html',{'form':fm})
   else:
      return HttpResponseRedirect('/login/')