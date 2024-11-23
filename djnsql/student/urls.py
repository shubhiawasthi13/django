from django.urls import path
from student.views import all_data, Reg_data

urlpatterns = [
    path('all/', all_data, name='alldata'),
    path('reg/', Reg_data, name='regdata'),
]
