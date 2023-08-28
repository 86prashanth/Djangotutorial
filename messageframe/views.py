from django.contrib import messages
from django.shortcuts import render
from messageframe.forms import MessageRegistrations

# Create your views here.
def reg(request):
    if request.method=='POST':
        fm=MessageRegistrations(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Your form has been submited..')
            messages.info(request,'now you can login')
            print(messages.get_level(request))
            messages.debug(request,'this is debug')
            messages.set_level(request,messages.DEBUG)
            print(messages.get_level(request))
            fm=MessageRegistrations()
    else:
        fm=MessageRegistrations()
    return render(request,'message/show.html',{'form':fm})