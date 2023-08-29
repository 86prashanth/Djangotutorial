from django.shortcuts import render

# Create your views here.
def one_to_one(request):
    return render(request,'model_relationship/onetoone.html')