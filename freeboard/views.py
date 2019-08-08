from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post
from .models import Comment

# Create your views here.
def freeboard(request):
    posts = Post.objects.all().order_by('-id')
    post_paginator = Paginator(posts, 15)
    page = request.GET.get('page')
    page_posts = post_paginator.get_page(page)
    return render(request, 'freeboard.html', {'page_posts' : page_posts})

def sort_freeboard(request):
    posts = Post.objects.all().order_by('-views')
    post_paginator = Paginator(posts, 15)
    page = request.GET.get('page')
    page_posts = post_paginator.get_page(page)
    return render(request, 'freeboard.html', {'page_posts' : page_posts})

def freeboardSearch(request):
    try:
        search_keyword = request.GET['input']
        condition = request.GET['condition']
    except:
        return redirec('freeboard')

    try:
        page = request.GET.get('page')
    except:
        page = request.GET['pagenum']

    if condition == 'titlesearch':
        searched_posts_objects = Post.objects.filter(title=search_keyword).order_by('-id')
        condition_to_korean = '글제목'
    elif condition == 'bodysearch':
        searched_posts_objects = Post.objects.filter(body__icontains=search_keyword).order_by('-id')
        condition_to_korean = '내용'
    else:
        searched_posts_objects = Post.objects.filter(owner=search_keyword).order_by('-id')
        condition_to_korean = '작성자'
        
    searched_paginator = Paginator(searched_posts_objects, 15)
    page = request.GET['pagenum']
    searched_posts = searched_paginator.get_page(page)
    return render(request, 'freeboardSearch.html', {'searched_posts' : searched_posts, 'searched_posts_objects' : searched_posts_objects,
                                                    'search_keyword' : search_keyword, 'condition' : condition, 'condition_to_korean' : condition_to_korean})

def sort_freeboardSearch(request):
    try:
        search_keyword = request.GET['input']
        condition = request.GET['condition']
    except:
        return redirec('freeboard')

    try:
        page = request.GET.get('page')
    except:
        page = request.GET['pagenum']

    if condition == 'titlesearch':
        searched_posts_objects = Post.objects.filter(title=search_keyword).order_by('-views')
        condition_to_korean = '글제목'
    elif condition == 'bodysearch':
        searched_posts_objects = Post.objects.filter(body__icontains=search_keyword).order_by('-views')
        condition_to_korean = '내용'
    else:
        searched_posts_objects = Post.objects.filter(owner=search_keyword).order_by('-views')
        condition_to_korean = '작성자'

    searched_paginator = Paginator(searched_posts_objects, 15)
    page = request.GET['pagenum']
    searched_posts = searched_paginator.get_page(page)
    return render(request, 'freeboardSearch.html', {'searched_posts' : searched_posts, 'searched_posts_objects' : searched_posts_objects,
                                                    'search_keyword' : search_keyword, 'condition' : condition, 'condition_to_korean' : condition_to_korean})

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

def deletepost(request, post_id):
    post = Post.objects.filter(id=post_id)
    post.delete()
    return redirect('freeboard')

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.increaseViews()
    return render(request,'detail.html',{'post' : post})

def writecomment(request, post_id):
    user = request.user
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment()
    comment.post = post
    comment.author = user.username
    comment.text=request.POST['comment']
    comment.save()
    return redirect('detail', post_id)

def deletecomment(request,post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail', post_id)

def editpost(request, post_id):
    editpost = Post.objects.get(id=post_id)
    print(editpost.title)
    print(editpost.body)
    return render(request,'editpost.html',{'editpost' : editpost})

def edit(request, post_id):
    editpost = Post.objects.get(id=post_id)
    editpost.title = request.POST['title']
    editpost.body = request.POST['body']
    editpost.save()
    print('수정합니다')
    return redirect('detail', post_id)