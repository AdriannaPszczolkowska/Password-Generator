from django.urls import path
from . import views


app_name = 'password'

urlpatterns = [
    path('', views.home, name ='home'),
    path('result', views.result, name='result'),
    path('about', views.about, name='about')
]