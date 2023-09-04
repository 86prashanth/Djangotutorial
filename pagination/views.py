from django.shortcuts import render
from pagination.models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import Http404
#Create your views here.
def post(request):
    post=Post.objects.all()
    paginator=Paginator(post,3,orphans=1) # if in case last 1 it will add last in 3
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    print('all_post',post)
    print('-------------------')
    print("paginator",paginator)
    print('----------------')
    print('page_obj',page_obj)
    # return render(request,'pagination/page.html',{'post':post})
    return render(request,'pagination/page.html',{'post':post,'page_obj':page_obj})


# class based view 
class PostListView(ListView):
    model=Post
    template_name='pagination/page_list.html'
    ordering=['id']
    paginate_by=3
    paginate_orphans=1
    
    def get_context_data(self,*args,**kwargs):
        try:
            return super(PostListView,self).get_context_data(*args,**kwargs)
        except Http404:
            self.kwargs['page']=1
            return super(PostListView,self).get_context_data(*args,**kwargs)

# detail view 
class PostDetailView(DetailView):
    model=Post 
    template_name='pagination/page_detail.html'