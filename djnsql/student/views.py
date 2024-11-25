from django.shortcuts import render
from student.models import Profile
from student.forms import Registraion
from django.http import HttpResponseRedirect

# Create your views here.

# insert  data using form api
def Reg_data(req):
    # reg_form = Registraion(label_suffix='----',initial={'email':'sonam@gmail.com'})
    if req.method == 'POST':
        form = Registraion(req.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            cty= form.cleaned_data['city']
            # save data
            user = Profile(name = nm,email =em,city = cty)
            user.save()
            return HttpResponseRedirect("/student/all/")
    else:
        form = Registraion()
    return render(req,'student/reg.html',{'form': form})



# show data
def all_data(req):
    all_students =Profile.objects.all()
    print(all_students)
    return render (req,'student/all.html',{'students':all_students})