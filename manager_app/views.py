from django.shortcuts import render
from manager_app.models import *
# Create your views here.
def manager_home(request):
    # objs=[
    #    Manager_student(name='prashanth',roll=101),
    #    Manager_student(name='kerala',roll=102),
    #    Manager_student(name='karimnage',roll=103),
    #    Manager_student(name='tanagalapally',roll=104),
    #    Manager_student(name='friend',roll=105),
    # ]
    # users=Manager_student.objects.bulk_create(objs) # bulk create
    # users=Manager_student.objects.all() # default manager 
    # users=Manager_student.students.all() # it will  change custom manager like students=models.Manager()
    # users=Manager_student.students.get_stu_roll_range(103,104)
    users=Proxystudent.students.get_stu_roll_range(103,104)
    return render(request,'manager_app/manager.html',{'users':users})