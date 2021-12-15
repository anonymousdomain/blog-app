from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.views.generic import (ListView,
                                  DetailView
                                  ,CreateView
                                  ,UpdateView
                                  ,DeleteView)
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
    paginate_by=6
class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by=5
    def get_queryset(self):
       user=get_object_or_404(User,username=self.kwargs.get('username'))
       return Post.objects.filter(author=user).order_by('-posted_date') 
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

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False 
    success_url='/' 
def about(request):
    return render(request, 'blog/about.html')
