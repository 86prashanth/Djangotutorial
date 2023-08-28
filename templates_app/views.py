from django.shortcuts import render

# Create your views here.
def learndj(request):
    return render(request,'course/courseone.html')

def coursetwo(request):
    return render(request,'course/coursetwo.html')

def feesone(request):
    return render(request,'fees/feesone.html')

def feestwo(request):
    return render(request,'fees/feestwo.html')