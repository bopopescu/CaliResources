from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import ListView, DetailView , CreateView ,UpdateView ,DeleteView
from .models import Post
from django.core.paginator import Paginator

def home(request):
    context = {

        'posts': Post.objects.all()
    }
          
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    #paginate_by = 2 
class PostDetailView(DetailView):
    model = Post 
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView ,UserPassesTestMixin):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    model = Post
    success_url = '/home'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

def about(request):
    return render(request,'blog/about.html')

