from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.core.cache import cache
from django.http import HttpResponse
from pagecounter import signals


# Create your views here.
def home(request):
    ct=request.session.get('count',0)
    newcount=ct+1
    request.session['count']=newcount
    return render(request,'pagecount/pagecounter.html',{'newcount':newcount})


def custom_signals(request):
    signals.notification.send(sender=None,request=request,user=['prashnth','nanda'])
    return HttpResponse("This is home page....")
# cache page

def cache_page(request):
    return render(request,'cache/course.html')


def contact_page(request):
    return render(request,'cache/contact.html')

def ip_address(request):
    ip=request.META.get('REMOTE_ADDR')
    print("clinet ip:",ip)
    request.session['ip']=ip
    return render(request,'signals/ip.html',{'ip':ip})

@receiver(user_logged_in,sender=User)
def login_count(sender,**kwargs):
    ct=cache.get('count',0,version=User.pk)
    newcount=ct+1
    print("sender:",sender)
    print(f'kwargs:{kwargs}')
    cache.set('count',newcount,60*60*24, version=User.pk)
    print(User.pk)
    return HttpResponse(f'the login count {newcount}')

    

