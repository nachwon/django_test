from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post.html', context)
