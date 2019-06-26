from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

__author__ = "suvorovao"


def posts(request):
    published_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/posts.html', {'posts': published_posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
