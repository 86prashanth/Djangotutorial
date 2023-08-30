from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from generic_listview.models import Student
# Create your views here.
class StudentDetailView(DetailView):
    model=Student
    template_name='detailview/detail.html'
    pk_url_kwarg='id'
    
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['all_student']=self.model.objects.all()    
        return context
        
class StudentListView(ListView):
    model=Student
    template_name='detailview/list.html'
    
