from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
from django.core.paginator import Paginator
from linkmoa import urlScrap
from linkmoa import dirManagement
from accounts import views
from .models import Memo
from .models import Profile

# Create your views here.
def board(request):
    user=request.user
    sort = request.GET.get('sort','')
    if sort == 'likes':
        memos = Memo.objects.filter(shared=True).order_by('-download')
    elif sort == 'mymemo':
        memos = Memo.objects.filter(shared=True, user_id=user.id).order_by('-id')
    else:
        memos = Memo.objects.filter(shared=True).order_by('-id')
    board_paginator = Paginator(memos, 20)
    page = request.GET.get('page')
    board_posts = board_paginator.get_page(page)
    return render(request,'board.html',{'board_posts' : board_posts})

def search(request):
    user=request.user
    keyword = request.POST['searchBox']
    sort = request.GET.get('sort','')
    if keyword =='':  #빈 input 예외처리
        return redirect('board')
    if keyword[0] == '#':  #태그 검색일 경우
        try:
            search_tag = keyword.replace("#","")
            tag=Tag.objects.get(name=search_tag)
            searched_memos = TaggedItem.objects.get_intersection_by_model(Memo, tag).filter(shared=True)
        except Tag.DoesNotExist:
            print('DoesNotExist')
            return render(request, 'search_board.html')
    else:   #일반 검색일 경우
        if sort == 'likes':
            searched_memos = Memo.objects.filter(keyword= keyword, shared=True).order_by('-download')
        elif sort == 'mymemo':
            searched_memos = Memo.objects.filter(keyword= keyword, shared=True, user_id=user.id).order_by('-id')
        else:
            searched_memos = Memo.objects.filter(keyword= keyword, shared=True).order_by('-id')
    search_paginator = Paginator(searched_memos, 20)
    page = request.GET.get('page')
    search_posts = search_paginator.get_page(page)
    return render(request,'search_board.html', {'search_posts' : search_posts})

def tag_board(request, tag):
    tag=Tag.objects.get(name=tag)
    tagged_memos = TaggedItem.objects.get_intersection_by_model(Memo, tag).filter(shared=True)
    tag_paginator = Paginator(tagged_memos, 20)
    page = request.GET.get('page')
    tag_posts = tag_paginator.get_page(page)
    return render(request, 'tag_board.html',{'tag_posts' : tag_posts})

def index(request):
    user=request.user
    print('Request user : ' + user.username)
    memos = Memo.objects.filter(user_id=user.id).order_by('-id')
    current = memos.filter(directory=user.profile.currentdir)
    paginator = Paginator(current, 20)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'index.html',{'memos' : memos, 'current' : current, 'userid' : user.id, 'posts' : posts})

def make_memo(request):
    user=request.user
    memo = Memo()
    splited = request.POST['url'].split('\n')
    filteredUrl = urlScrap.scrapUrl(splited, memo.keyword)
    if len(filteredUrl) > 1:
        memo.updateMemo(user.id, user.username, "recently", False, 0, request.POST['key'], filteredUrl, "", "")
    return redirect('index')

def mkdir(request):
    user=request.user
    dname = request.POST['dirname']
    if user.profile.numofDir == 10:
        print('디렉토리 최대 개수는 10 개 입니다.')
    else:
        a = dirManagement.makeDirectory(user,dname)
        if a == 0:
            print('같은 이름의 디렉토리를 생성 할 수 없습니다.')
    return redirect('index')

def changedir(request, cddir):
    user=request.user
    user.profile.currentdir=cddir
    user.profile.save()
    return redirect('index')

def changedirname(request, dirname):
    user=request.user
    newname = request.GET.get('changename')
    if user.profile.currentdir == dirname:
        user.profile.currentdir = newname
        user.profile.save()
    dirMemo = Memo.objects.filter(directory=dirname)
    dirManagement.changedirname(user, dirname, newname, dirMemo)
    return redirect('index')

def deletedir(request, dirname):
    user=request.user
    dname = dirname
    memos = Memo.objects.filter(user_id=user.id, directory=dirname)
    memos.delete()
    dirManagement.deleteDirectory(user, dname)
    return redirect('index')

def delete_memo(request, memo_id):
    user=request.user
    memo = Memo.objects.get(id=memo_id)
    memo.delete()
    return redirect('index')

def share_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    memo.shared = True
    memo.save()
    return redirect('index')

def edit_memo(request, memo_id):
    user=request.user
    memo = Memo.objects.get(id=memo_id)
    memo.updateMemo(user.id, user.username, memo.directory, memo.shared, memo.download, request.GET.get('editKey'), request.GET.get('editUrl'), request.GET.get('editMemo'), request.GET.get('editTag').replace("#",","))
    return redirect('index')

def undo_share(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    memo.shared = False
    memo.download = 0
    memo.save()
    return redirect('/')

def download_memo(request, memo_id):
    user=request.user
    newMemo = Memo()
    oldMemo = Memo.objects.get(id=memo_id)
    oldMemo.increaseDL()
    newMemo.updateMemo(user.id, user.username, 'recently', False, 0, oldMemo.keyword, oldMemo.urls, "","")
    return redirect('index')

def movedir(request, memo_id, dirname):
    user = request.user
    memo = Memo.objects.get(id=memo_id)
    setattr(memo, 'directory', dirname)
    memo.save()
    return redirect('index')

#Deprecated function
# def appear_memo(request, memo_id):
#     memo = Memo.objects.get(id=memo_id)
#     memo.display='visible'
#     memo.save()
#     return redirect('index')

# def disappear_memo(request, memo_id):
#     memo = Memo.objects.get(id=memo_id)
#     memo.display='invisible'
#     memo.save()
#     return redirect('index')