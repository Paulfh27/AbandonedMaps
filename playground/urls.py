from django.urls import path
from . import views

# URLConfing 
urlpatterns = [
    path('hello/', views.sayHello)
]