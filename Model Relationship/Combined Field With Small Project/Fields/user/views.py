from django.shortcuts import render
from .models import Page,Post,Song,User
# Create your views here.

def home(request):
    return render(request,'user/home.html')

def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email='Admin@gmail.com')
    data3 = User.objects.filter(page__page_cat='C++')
    data4 = User.objects.filter(post__post_pub_date='2023-09-02')
    data5 = User.objects.filter(song__song_duration=2)
    return render(request,'user/user.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})
    