from django.shortcuts import render
from model_inheritance.models import *
# Create your views here.
def home(request):
    student_data=Student.objects.all()
    teacher_data=Teacher.objects.all()
    contract_data=Contractor.objects.all()
    examcenter=Examcenter.objects.all()
    myexamcenter=MyExamcenter.objects.all()
    studentcenter=Studentcenter.objects.all()
    return render(request,'inheritance/inheritance.html',{'student_data':student_data,
                                                          'teacher_data':teacher_data,
                                                          'contract_data':contract_data,
                                                          'examcenter':examcenter,
                                                          'studentcenter':studentcenter,
                                                          'myexamcenter':myexamcenter})
    