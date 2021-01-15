from django.urls import path
from . import views #from all import views	
urlpatterns = [
   path('', views, name='index'),
  ]
