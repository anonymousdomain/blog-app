from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.views.generic import (ListView,
                                  DetailView
                                  ,CreateView
                                  ,UpdateView)
from .models import Post
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model=Post
    #modify the template pattern that list view class excpect
    template_name='blog/home.html'
    context_object_name='posts'
    #post ordered by latest time post
    ordering=['-posted_date']
class PostDetailView(DetailView):
    model=Post
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
    
def about(request):
    return render(request, 'blog/about.html')
