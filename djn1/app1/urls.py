from django.urls import path
from app1.views import home, skill
urlpatterns = [
    path('home/',home,name='home'),
    path('skill/',skill,name='skill'),
    
]
