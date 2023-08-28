from django.shortcuts import HttpResponse,render
# def my_middleware(get_response):
#     print("one time initalization...")
#     def my_function(request):
#         print("this is before view...")
#         response=get_response(request)
#         print("this is after view...")
#         return response 
#     return my_function


class Brothermiddleware:
    def __init__(self,get_response):
        self.get_response=get_response 
        print("one time brother initialization...")
    def __call__(self,request):
        print("this is brother before view...")
        response=self.get_response(request)
        print("this is brother after view..")
        return response
        
class Mothermiddleware:
    def __init__(self,get_response):
        self.get_response=get_response 
        print("one time mother initialization...")
    def __call__(self,request):
        print("this is mother before view...")
        response=self.get_response(request)
        print("this is mother after view..")
        return response    
        
class Fathermiddleware:
    def __init__(self,get_response):
        self.get_response=get_response 
        print("one time father initialization...")
    def __call__(self,request):
        print("this is father before view...")
        response=self.get_response(request)
        print("this is father after view..")
        return response
    
class Myprocessmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response 
        
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_view(request,*args,**kwargs):
        print("this is process view...")
        # return HttpResponse("this is before view...")
        return None
    
class MyExceptionmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response 
        
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_excception(self,request,exception):
        msg=exception
        class_name=exception.__class__.name
        print(class_name)
        print(msg)
        return HttpResponse(msg)
    
    
    
class MyTemplatemiddleware:
    def __init__(self,get_response):
        self.get_response=get_response 
        
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_template_response(self,request,response):
        print("process template response from middleware..")
        response.context_data['name']='sonam'
        return response
        # return None
        # print("this is exception view...")
        # return HttpResponse("this is before view...")
        # return None
class UnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response 
    def __call__(self,request):
        # print("call from middelware before view..")
        response=render(request,'core/underconstruction.html')
        # response=HttpResponse("this is under construction...")
        print("call from middlware after view")
        response=self.get_response(request)
        return response 
    