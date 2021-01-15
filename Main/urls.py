from django.urls import path
from . import views #from all import views	
urlpatterns = [
   path('', views.index, name='index'),
   path('about', views.about, name='about'),
   path('contact', views.contact, name='contact'),
   path('faq', views.faq, name='faq'),
   path('shop', views.shop, name='shop'),
  ]
