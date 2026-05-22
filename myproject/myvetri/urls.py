from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('web/', views.web, name='web'),
    path('software/', views.software, name='software'),
    path('digital/', views.digital_marketing, name='digital'),
]
