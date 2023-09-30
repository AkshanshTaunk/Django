from django.shortcuts import render
from .models import Post
# Create your views here.
def Post_list(request):
    all_post=Post.objects.all()
    return render(request,'myapp/home.html',{'posts':all_post})