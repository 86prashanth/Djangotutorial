from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

# Create your views here.
@login_required
def profile(request):
    return render(request,'registration/profile.html',{'name':request.user})


# class ProfileTemplateView(TemplateView):
#     template_name='registration/profileview.html'
@method_decorator(login_required,name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name='registration/profileview.html'
    
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args,**kwargs)

@staff_member_required
def about(request):
    return render(request,'registration/about.html')

# class AboutTemplateView(TemplateView):
#     template_name='registration/aboutview.html'
@method_decorator(staff_member_required,name='dispatch')
class AboutTemplateView(TemplateView):
    template_name='registration/aboutview.html'