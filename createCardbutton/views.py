from django.shortcuts import render
from django.views import View
from .models import Product

class ProductView(View):
    def get(self, request):
        all_product = Product.objects.all()
        context = {'products':all_product}
        return render(request,'createcard/product-card.html', context)

class ProductFilter(View):
    def get(self, request, name):
        print(name)
        product = Product.objects.get(product_name = name)
        context = {'product': product}
        return render(request,'createcard/product_page.html',context)