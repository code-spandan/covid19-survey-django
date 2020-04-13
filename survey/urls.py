from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                              #Adding view function index to main page of our app i.e "survey/"
    path('main/', views.formmain),                      #Adding view function formmain to the "survey/main/" path
    path('main/second/', views.formsecond)              #Adding the view funtion formsecond to the "survey/main/second/" path
]