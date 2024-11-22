from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def dtl(req):
    # filters.....................................................
    # name = "django"
    # duration = "four months"
    # desc = "Heloo this is app2 "
    # course_details = {"nm":name,'dur':duration,"desc":desc}
    # return render(req,'app2/dtl.html',context=course_details)

    # datetime....................................................
    # dt= datetime.now()
    # return render(req,'app2/dtl.html',context={"dt":dt})

    # float formate...............................................
    # return render(req,'app2/dtl.html',context={"p1": 10.00,"p2":57.789,"p3":45.900})

    # if tag......................................................
    # return render(req,'app2/dtl.html',context={"name":'django'})
     
    # for loop..... ..............................................
    # student = {'names': ['rahul','sonam','aditya']}
    # return render(req,'app2/dtl.html',context=student)
    
    # complex data................................................

    stu = {"stu1":{"name":'rahul',"age":37},
           "stu2":{"name":"ajay","age":33},
           "stu3":{"name":"vinay","age":38},
    }
    students = {"student": stu}
    
    return render(req,'app2/dtl.html',context=students)

def django(request):
    return render (request,'app2/django.html')

    
