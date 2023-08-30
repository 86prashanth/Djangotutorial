from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from class_based_view.forms import *
# Create your views here.
# function based view 
def myview(request):
    return HttpResponse('<h1>Function based view</h1>')

# classbasedview 
class MyView(View):
    name='class_based_view'
    # name=''
    def get(self,request):
        # return HttpResponse("<h2>Class Based View</h2>")
        return HttpResponse(f'name:{self.name}')
    
class MyViewChild(MyView):
    def get(self,request):
        print(self.name)
        return HttpResponse(self.name)
    
class HomeClassView(View):
    def get(self,request):
        return render(request,'cbv/home.html')

def aboutfun(request):
    context={'msg':'welcome to function based view...'}
    return render(request,'cbv/about.html',context)

class AboutClassView(View):
    def get(self,request):
        context={'msg':'welcome to class based view..'}
        return render(request,'cbv/about.html',context)
    
# function based view forms 
def contactfun(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('thank form has been submiited')
    else:
        form=ContactForm()
    return render(request,'cbv/contact.html',{'form':form})
################################################
# classbased view form
class ContactClassView(View):
    def get(self,request):
        form=ContactForm()
        return render(request,'cbv/contact.html',{'form':form})
    def post(self,request):
        form=ContactForm()
        if form.is_valid():
            print(form.cleaned_data['name'])
        return HttpResponse('Thank you submitted..')
    
# news function based view
def newsfun(request,template_name):
    template_name=template_name
    context={'info':'cbi enquiry why earns less money'}
    # return render(request,'cbv/news.html',context)
    return render(request,template_name,context)

# news classbased view 
class NewsClassView(View):
    # template_name='cbv/news.html'
    template_name=''
    def get(self,request):
        context={'info':'cbi enquiry earn less money'}
        # return render(request,'cbv/news.html',context)
        return render(request,self.template_name,context)