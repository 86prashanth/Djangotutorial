from django.shortcuts import render
from django.http import HttpResponse
from generic_listview.models import Student
from django.views.generic.list import ListView
# Create your views here.
class StudentListView(ListView):
    model=Student
    template_name='generic_listview/student.html' 
    # ordering=['name']
    # context_object_name='students'
    
    # template_name_suffix='_get' # student_get.html
    # template_name_suffix='' # student.html
    # student_list=Student.objects.all()
    # context={'student_list':student_list}
    # return render(request,'listview/list_view.html',context)
    
    def get_queryset(self):
        return Student.objects.filter(course='python')
    
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['freshers']=Student.objects.all().order_by('name')
        return context
    
    def get_template_name(self):
        if self.request.COOKIE['user']=='user':
            template_name='generic_listview/user.html'
        else:
            template_name=self.template_name
        return [template_name]
    
    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name='generic_listview/superuser.html'
        elif self.request.user.is_staff:
            template_name='generic_listview/staff.html'
        else:
            template_name=self.template_name
        return [template_name]