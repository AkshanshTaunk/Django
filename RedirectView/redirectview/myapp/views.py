from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.

class YoutubeRedirectView(RedirectView):
    url='https://www.youtube.com'