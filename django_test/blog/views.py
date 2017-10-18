from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post


def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        author = User.objects.get(username='nachwon')
        title = request.POST['title']
        photo = request.FILES.get('photo')

        content = request.POST['content']
        Post.objects.create(
            author=author,
            title=title,
            photo=photo,
            content=content,
        )
        return redirect(blog_index)
    else:
        return render(request, 'blog/post_create.html')
