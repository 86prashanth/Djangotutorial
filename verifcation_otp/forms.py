from django import forms 
from verifcation_otp.models import Code 

class CodeForm(forms.ModelForm):
    number=forms.CharField(label='Code',help_text='Enter sms verfication')
    class Meta:
        model=Code 
        fields=('number',)