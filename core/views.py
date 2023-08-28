from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from datetime import datetime,timedelta
from django.core import signing
# Create your views here.
def learndj(request):
    return HttpResponse("learn django..")

def learnpython(request):
    return HttpResponse('learn python...')

def staticapp(request):
    return render(request,'core/static.html')

def setcookie(request):
    response=render(request,'cookie/setcookie.html')
    response.set_signed_cookie('name','guest',salt='nm',expires=datetime.utcnow()+timedelta(days=2))
    response.set_cookie('name','prashanth')
    return response


def getcookie(request):
    name=request.COOKIES['name']
    # name=request.get_signed_cookie('name',salt='nm')
    return render(request,'cookie/getcookie.html',{'name':name})
# def getcookie(request):
#     # name=request.COOKIES['name']
#     # name=request.COOKIES.get('name')
#     # name=request.COOKIES.get('name','guest',max_age=60,==salt="name",expires=datetime.utcnow()+timedelta())
#     name=request.get_signed_cookie('name',salt='nm')
#     return render(request,'cookie/getcookie.html',{'name':name})

def deletecookie(request):
    response=render(request,'cookie/deletecookie.html')
    response.delete_cookie('name')
    return response

def setsession(request):
    request.session['name']='prsahnth'
    # request.session.set_expiry(0)
    # request.session.set_expiry(5)
    # request.session['lname']='rajinikanth'
    return render(request,'session/setsession.html')


def getsession(request):
    # name=request.session['name']
    # name=request.session.get('name')
    if 'name' in request.session:
        name=request.session['name']
        request.session.modified=True
    # keys=request.session.keys()
    # items=request.session.items()
    # age=request.session.setdefault('age','26')
    
        print(request.session.get_session_cookie_age())
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        print(request.session.get_expire_at_browser_close())
    
    # lname=request.session.get('lname')
    # return render(request,'session/getsession.html',{'name':name,'lname':lname})
    # return render(request,'session/getsession.html',{'name':name,'keys':keys,'items':items,'age':age})
        return render(request,'session/getsession.html',{'name':name})
        # return render(request,'session/getsession.html')
    else:
        return HttpResponse('your session has been expired...')

                                                     
def deletesession(request):
    request.session.flush()
    request.session.clear_expired()
    # if 'name' in request.session:
    #     del request.session['name']
    return render(request,'session/deletesession.html')
    
def mid_ware(request):
    print("i am view..")
    return HttpResponse("This is middleware...")


def mymidware(request):
    print("my middleware...")
    return HttpResponse("my middleware...")

def myprocess(request):
    print("my process..")
    return HttpResponse("my process view..")

def myexception(request):
    print('exception...')
    a=10/0
    return HttpResponse('this is exception page.....')

def user_info(request):
    print("i am user info view..")
    context={'name':'rahul'}
    return TemplateResponse(request,'core/user.html',context)

def undercon(request):
    return render(request,'core/underconstruction.html')
