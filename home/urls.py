from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('blog-1', views.blog1, name='blog-1')
]
