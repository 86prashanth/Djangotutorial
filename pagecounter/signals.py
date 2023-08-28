from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.shortcuts import render
from django.dispatch import receiver,Signal
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete
from django.core.signals import request_started,request_finished,got_request_exception




notification=Signal()

@receiver(notification)
def show_notification(sender,**kwargs):
    print("sender:",sender)
    print(f'kwargs{kwargs}')
    print("notification...")

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("------------")
    print("logged in signal.. run intro..")
    print('sender:',sender)
    print('request:',request)
    print('user:',user)
    print(f'kwargs:{kwargs}')
    # user_logged_in.connect(login_success,sender=User)
    
@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("-----------------------------")
    print("logged-out signal.. run out..")
    print("sender:",sender)
    print("request:",request)
    print("User:",user)
    print('user password:',user.password)
    print(f'kwargs:{kwargs}')

@receiver(user_login_failed)
def login_failed(sender,request,credentials,**kwargs):
    print("------------------")
    print("login failed signal ----")
    print('sender:',sender)
    print("request:",request)
    print("Credentials:",credentials)
    print(f'kwargs:{kwargs}')
    
    
    
@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("--at beginning save--")
    print('pre save signal...')
    print("sender:",sender)
    print("instance:",instance)
    print(f'kwargs:{kwargs}')
    
    
@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("--------------------------")
        print("post save signal...")
        print("new record")
        print("sender:",sender)
        print("instance:",instance)
        print("created:",created)
        print(f'kwargs:{kwargs}')
    else:
        print("------------------------")
        print("post save signal...")
        print("update")
        print("sender:",sender)
        print("instance:",instance)
        print("created:",created)
        print(f'kwargs:{kwargs}')
        
        
@receiver(pre_delete,sender=User)
def at_begining_delete(sender,instance,**kwargs):
    print("------------------")
    print("at pre delete..")
    print("sender:",sender)
    print("instance:",instance)
    print(f'kwargs:{kwargs}')
    
@receiver(post_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("-----------------")
    print("post delete..")
    print("sender:",sender)
    print("instance:",instance)
    
    
    
@receiver(pre_init,sender=User)
def at_begining_init(sender,*args,**kwargs):
    print("------------------")
    print("at pre init....")
    print("sender:",sender)
    print(f'kwargs:{args}')
    print(f'kwargs:{kwargs}')
    
@receiver(post_init,sender=User)
def at_ending_init(sender,*args,**kwargs):
    print("-----------------")
    print("post init..")
    print(f'args:{args}')
    print(f'kwargs:{kwargs}')

    
@receiver(request_started)
def at_begining_request(sender,environ,**kwargs):
    print("--------------------")
    print("At begining request..")
    print("Sender:",sender)
    print("enviorn:",environ)
    print(f'kwargs:{kwargs}')
    
@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print("---------------------")
    print("at ending request...")
    print("sender:",sender)
    print(f'kwargs:{kwargs}')