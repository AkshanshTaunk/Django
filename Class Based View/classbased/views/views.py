from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
# Create your views here.

# class MyView(View):
#     name='Akshansh'
#     def get(self,request):
#         return HttpResponse(self.name)

# class MyViewChild(MyView):
#     def get(self):
#         return HttpResponse(self.name)

#     FUNCTION BASED
# def home(request):
#     return render(request,'views/home.html')

class MyView(View):
    def get(self,request):
        context = {'msg':'Hello guys welcome to django framework'}
        return render(request,'views/home.html',context)

#     FUNCTION BASED

# def contactform(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.cleaned_data['name']
#             return HttpResponse('Thank you for submission')
#     else:
#         form = ContactForm()
#     return render(request,'views/contact.html',{'fm':form})

class ContactFormView(View):
    def get(self,request):
        form = ContactForm()
        return render(request,'views/contact.html',{'form':form})
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you for submission')

class NewsView(View):
    def get(self,request):
        template_name = 'views/news.html'
        context = {'info':"CBI enquiry held today on goverment office"}
        return render(request,template_name,context)