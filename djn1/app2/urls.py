from django.urls import path
from app2.views import dtl,django
urlpatterns = [
    path('dtl/',dtl),
    path('dj/',django,name='dj')
    
]