from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
from django.core.paginator import Paginator
from django.http import Http404
# Create your FunctionBasedviews here.
# def Post_list(request):
#     all_post=Post.objects.all().order_by('id')
#     paginator = Paginator(all_post,2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request,'myapp/home.html',{'page_obj':page_obj})

class PostListView(ListView):
    model = Post
    template_name = 'myapp/home.html'
    ordering = ['id']
    paginate_by = 2
    paginate_orphans = 1

    def get_context_data(self, *args, **kwargs):
        try:
            return super(PostListView,self).get_context_data(*args,**kwargs) 
        except Http404:
            self.kwargs['page']=1
            return super(PostListView,self).get_context_data(*args,**kwargs)

class PostDetailView(DetailView):
    model=Post
    template_name = 'myapp/post.html'
