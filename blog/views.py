from django.shortcuts import render

__author__ = "suvorovao"


def posts(request):
    return render(request, 'blog/posts.html', {})
