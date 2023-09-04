from django.shortcuts import render
from django.http import response
from rest_framework.decorators import api_view 
from Otp_Verfication.helpers import send_otp_to_phone
from Otp_Verfication.models import User
# Create your views here.
@api_view(['POST'])
def send_otp(request):
    data=request.data
    if data.get('phone_number') is None:
        return response({
            'status':400,
            'message':'key phone_number is required'
        })
    if data.get('passwordd') is None:
        return response({
            'status':400,
            'message':'key password is required'
        })
    user=User.objects.create(phone_number=data.get('phone_number'),
                             otp=send_otp_to_phone(data.get('phone_number')))
    user.set_password=data.get('set_password')
    user.save()
    return Response({
        'status':200,'message':'Otp has been sent'
    })
    