from django.urls import path
from Register import views

urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('sign', views.sign, name='sign'),
]
