from django.shortcuts import render
from dynamicapp.models import *
# Create your views here.
def learn_django(request):
    context={'cname':'django'}
    name={'names':['hi','bye','tata']}
    
    stu={'stu1':{'name':'rahul','roll':101},
         'stu2':{'name':'sachin','roll':98},
         'stu3':{'name':'raj','roll':103},
         'stu4':{'name':'anu','roll':104}
         },
    students={'students':stu}

    # return render(request,'dynamic/home.html',context)
    # return render(request,'dynamic/home.html',name)
    return render(request,'dynamic/home.html',students)

def course_details(request):
    cname='django'
    duration='4months'
    seats=20
    django_details={'cname':cname,'duration':duration,'seats':seats}
    return render(request,'dynamic/course_details.html',django_details)


def models(request):
    student=Student.objects.all()
    students={'student':student}
    return render(request,'models/students.html',students)