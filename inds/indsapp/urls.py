from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('industries', views.industries, name='industries'),
    path('main', views.main, name='main'),
    path('single', views.single, name='single'),
    path('work', views.work, name='work'),
]
