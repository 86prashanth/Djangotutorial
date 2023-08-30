from django.views.generic.edit import DeleteView
from modelformmixin.models import Student

class StudentDeleteview(DeleteView):
    model=Student
    success_url='/mixin/create/'
    template_name='mixin/confirm_delete.html'
    