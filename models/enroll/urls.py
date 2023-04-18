from django.urls import path
from . import views

urlpatterns = [
        path('reg/<int:my_id>/',views.showformdata,name="detail"),
]
