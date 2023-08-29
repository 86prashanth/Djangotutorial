from django.shortcuts import render
from querysetapi.models import Student,Teacher
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count
from datetime import date,time
# Create your views here.
def home(request):
    
    users=Student.objects.all() # all data display
    # users=Student.objects.filter(marks=70) # no data found
    # users=Student.objects.exclude(marks=80) #  exclude 70 marks # 
    # users=Student.objects.order_by('name') # order by name ascending
    # users=Student.objects.order_by('-name') # order by name descending
    # users=Student.objects.order_by('?') # random only 
    # users=Student.objects.reverse() # reverse
    # users=Student.objects.order_by('id').reverse() # reverse
    # users=Student.objects.order_by('id').reverse()[0:5] # reverse last 5 columns
    # users=Student.objects.values() # values display
    # users=Student.objects.values('name','city') # value display 
    # users=Student.objects.values_list('id','name',named=True) # empty values display
    # users=Student.objects.using('default') # using default
    # users=Student.objects.dates('pass_date','month') # passing date
    # users=Student.objects.dates('pass_date','year') # passing date
    # users=Student.objects.none() # empty results
    # users=Student.objects.all()
    # users2=Teacher.objects.all()
    # users=Student.objects.values_list('id','name',named=True)
    # users2=Teacher.objects.values_list('id','name',named=True)
    # data=users.union(users2)  # union table
    # users=Student.objects.values_list('id','name',named=True)
    # users2=Teacher.objects.values_list('id','name',named=True)
    # # data=users.intersection(users2) # intersection table
    # users=Student.objects.values_list('id','name',named=True)
    # users2=Teacher.objects.values_list('id','name',named=True)
    # data=users.difference(users2) # difference table
    # users=Student.objects.filter(id=6) & Student.objects.filter(roll=106) 
    # users=Student.objects.filter(id=6,roll=106) 
    # users=Student.objects.filter(Q(id=6)&Q(roll=106)) # q operators
    # users=Student.objects.filter(Q(id=6) | Q(roll=106)) # q operators
    # users=Student.objects.filter(id=6)|Student.objects.filter(roll=106)
    
    print("--------------")
    print("return:",users)
    # print("return:",users)
    print("----------------")
    # print("sql query:",users.query)
    return render(request,'queryset/home.html',{'users':users})
    # return render(request,'queryset/home.html',{'users':users,'users2':users2,'data':data})
    
    
# def queryset(request,pk):
def queryset(request):
    # users=Student.objects.filter(id=pk)
    # users=Student.objects.get(id=1) # id first
    # users=Student.objects.get(name='mahesh') # name mahesh
    # users=Student.objects.first() # first
    # users=Student.objects.order_by('name').first() # assending after first
    # users=Student.objects.latest('pass_date') # latest data
    # users=Student.objects.earliest('pass_date') # earlist data
    # users=Student.objects.all()
    # one_data=Student.objects.get(pk=1)
    # print(users.filter(pk=one_data.pk).exists())
    # print(users.exists())
    # users=Student.objects.create(name='sameer',roll=109,city='bro',marks=76,pass_date='2023-08-09') #  create data
    # users ,created=Student.objects.get_or_create(name='karna',roll=110,city='bro',marks=76,pass_date='2023-08-09') # get or create data
    # print(created)
    # users=Student.objects.filter(id=10).update(city="brother")
    # users, createad=Student.objects.update_or_create(id=4,name='sonam',defaults={'name':'kiran'})
    # print(createad) # update and create
    # bulk create
    # objs=[
    #     Student(name='prashanth',roll=101,city='dehradun',marks=30,pass_date='2023-05-23'),
    #     Student(name='karthikeya',roll=102,city='rajastan',marks=50,pass_date='2023-08-23'),
    #     Student(name='laptop',roll=104,city='vali',marks=60,pass_date='2021-05-23'),
    #     Student(name='cabel',roll=105,city='chennai',marks=70,pass_date='2024-05-23'),
    #     Student(name='kiran',roll=106,city='dehradun',marks=30,pass_date='2023-05-23'),
    #     Student(name='rivar',roll=107,city='rajastan',marks=50,pass_date='2023-08-23'),
    #     Student(name='lenovo',roll=108,city='vali',marks=60,pass_date='2021-05-23'),
    #     Student(name='casio',roll=109,city='chennai',marks=70,pass_date='2024-05-23'),
    # ]
    # users=Student.objects.bulk_create(objs) # bulk create
    # bulk update
    # users=Student.objects.all()
    # for stu in users:
    #     stu.city='hyderabad'
    # users=Student.objects.bulk_update(user,['city']) 
    # users=Student.objects.in_bulk([1,2])
    # print(users[1].name)
    # users=Student.objects.in_bulk()
    # users=Student.objects.get(pk=13).delete() # single record delete
    # users=Student.objects.filter(marks=30).delete()  # marks as 30 all record will be delete
    # users=Student.objects.all().delete()
    # deleted=users.delete()
    # print(deleted) 
    users=Student.objects.all()
    # print(users.count())
    # print(users.explain())
    print("return:",users)
    return render(request,'queryset/queryset.html',{'users':users})



def fieldlookup(request):
    # users=Student.objects.all()
    # users=Student.objects.filter(name__exact='cabel')  # exactly match
    # users=Student.objects.filter(name__iexact='Cabel') # in capital ,small letter match
    # users=Student.objects.filter(name__contains='c')  # name contains c with start
    # users=Student.objects.filter(id__in=[16,19,22]) # id 16,19,22
    # users=Student.objects.filter(marks__in=[60,30]) #  60 30
    # users=Student.objects.filter(marks__gt=60)
    # users=Student.objects.filter(marks__gte=60)
    # users=Student.objects.filter(marks__lt=60)
    # users=Student.objects.filter(marks__lte=60)
    # users=Student.objects.filter(name__startswith='l')
    # users=Student.objects.filter(name__istartswith='L')
    # users=Student.objects.filter(name__endswith='l')
    # users=Student.objects.filter(name__iendswith='l')
    # users=Student.objects.filter(pass_date__range=('2023-01-01','2023-08-31'))

    # users=Student.objects.filter(pass_date__year=2023)
    # users=Student.objects.filter(pass_date__year__gte=2023)
    # users=Student.objects.filter(pass_date__month__gte=4)
    # users=Student.objects.filter(pass_date__month__gt=4)
    # users=Student.objects.filter(pass_date__day=2)
    # users=Student.objects.filter(pass_date__day__gt=2)
    # users=Student.objects.filter(pass_date__week=13)
    # users=Student.objects.filter(pass_date__week__gt=13)
    # users=Student.objects.filter(pass_date__week_day=13)
    # users=Student.objects.filter(pass_date__quarter=2)
    # users=Student.objects.filter(pass_date__time_gt=time(21,17))
    # users=Student.objects.filter(pass_date__hour__gt=5)
    # users=Student.objects.filter(pass_date__minute__gt=20)
    users=Student.objects.filter(pass_date__second__gt=20)
    print("return",users)
    print('------------------')
    print('sql query',users.query)
    return render(request,'queryset/fieldlookup.html',{"users":users})

def agree(request):
    users=Student.objects.all()
    average=users.aggregate(Avg('marks'))
    sum=users.aggregate(Sum('marks'))
    min=users.aggregate(Min('marks'))
    max=users.aggregate(Max('marks'))
    count=users.aggregate(Count('marks'))
    print('-------------------')
    print(average)
    print(max)
    print(sum)
    print(min)
    print(count)
    context={'users':users,'average':average,'sum':sum,'min':min,'max':max,'count':count}
    return render(request,'queryset/agree.html',context)

def Qobject(request):
    # users=Student.objects.all()
    # users=Student.objects.all()[:5] # limit
    # users=Student.objects.all()[5:10] # limit
    users=Student.objects.all()[:11:2] # limit
    # users=Student.objects.filter(Q(id=24) & Q(roll=101))
    # users=Student.objects.filter(Q(id=24) | Q(roll=101))
    # users=Student.objects.filter(~Q(id=24))
    return render(request,'queryset/qobject.html',{'users':users})