from django import forms 
from messageframe.models import Messagesframe


class MessageRegistrations(forms.ModelForm):
    class Meta:
        model=Messagesframe
        fields=['name','email','password']