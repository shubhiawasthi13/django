from django.shortcuts import render
from student.models import Profile
from student.forms import Registraion

# Create your views here.
def all_data(req):
    all_students =Profile.objects.all()
    print(all_students)
    return render (req,'student/all.html',{'students':all_students})

def Reg_data(req):
    reg_form = Registraion(label_suffix='----',initial={'email':'sonam@gmail.com'})
    return render(req,'student/reg.html',{'form': reg_form})