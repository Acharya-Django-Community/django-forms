from django.shortcuts import render , get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request,'home.html',context)

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        'post': post
    }
    return render(request,'post_detail.html',context)