from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post, Category, Reply
from django.contrib.auth.decorators import login_required

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5



class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'



