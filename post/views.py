from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def create_post(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = Post.create(
                postForm.data['title'], postForm.data['content'])
            post.save()
        return redirect('/post/')
    else:
        return render(request, 'post_create.html')


def detail_post(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'title': post.title,
        'content': post.content
    }
    return render(request, 'post_detail.html', context)


def edit_post(request, id):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = Post.objects.get(pk=id)
            post.title = postForm.data['title']
            post.content = postForm.data['content']
            post.save()
        return redirect('/post/')
    else:
        post = Post.objects.get(pk=id)
        context = {
            'id': post.id,
            'title': post.title,
            'content': post.content
        }
        return render(request, 'post_edit.html', context)


def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('/post/')
