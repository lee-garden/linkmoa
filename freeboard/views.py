from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def freeboard(request):
    posts = Post.objects.all().order_by('-id')
    post_paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    page_posts = post_paginator.get_page(page)
    return render(request, 'freeboard.html', {'page_posts' : page_posts})

def newpost(request):
    print('new post')
    return render(request, 'newpost.html')

def createpost(request):
    print('create post')
    user = request.user
    post = Post()
    post.user_id = user.id
    post.owner = user.username
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('freeboard')

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.increaseViews()
    return render(request,'detail.html',{'post' : post})