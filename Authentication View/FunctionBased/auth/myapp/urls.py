from django.urls import path
from myapp import views

urlpatterns = [
    path('profile/',views.ProfileTemplateView.as_view(),name='profile')
]