from django.shortcuts import render,HttpResponse
from .forms import ContactForm, FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.

class ContactFormView(FormView):
    template_name = 'myapp/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'
    def form_valid(self,form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        # return super().form_valid(form)
        return HttpResponse('msg sent successfully!!!!!!!!!!!!!!!!!!')


class ThanksTemplateView(TemplateView):
    template_name = 'myapp/template.html'