from django.urls import path
from .import views
 
urlpatterns=[
    path('', views.index),
    path('register', views.user_reg),
    path("login",views.login)
]