from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based view
def home(request):
    # a='<h1> hello varaible</h1>'
    # a=10+10
    a='function based view'
    # return HttpResponse(f'this is function based view {a}')
    return HttpResponse(a)
    # return HttpResponse("Hello djagno"
    
def home2(request):
    return render(request,'hyperlinks/home2.html')

def hyperlinks(request):
    return render(request,'hyperlinks/hyperlinks.html')

def about(request):
    return render(request,'hyperlinks/about.html')

def contact(request):
    return render(request,'hyperlinks/contact.html')
