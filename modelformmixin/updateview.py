from django.views.generic.edit import CreateView
from modelformmixin.models import Student
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView

class StudentUpdateCreateView(CreateView):
    model=Student
    template_name='mixin/create_form.html'
    fields=['name','email','password']

class StudentUpdateView(UpdateView):
    model=Student
    fields=['name','email','password']
    template='mixin/update_form.html'
    success_url='/mixin/thanksupdate/'
    
class ThanksUpdateview(TemplateView):
    template_name='mixin/thanksupdate.html'