from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import ListView, DetailView , CreateView ,UpdateView ,DeleteView
from .models import Post
from django.core.paginator import Paginator

def home(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'posts': posts})

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

