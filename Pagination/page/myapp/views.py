from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.
def Post_list(request):
    all_post=Post.objects.all().order_by('id')
    paginator = Paginator(all_post,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'myapp/home.html',{'page_obj':page_obj})