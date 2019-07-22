from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
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
        return render(request,'board.html',{'memos' : memos})
    elif sort == 'mymemo':
        memos = Memo.objects.filter(shared=True, user_id=user.id).order_by('-id')
        return render(request,'board.html',{'memos' : memos})
    memos = Memo.objects.filter(shared=True).order_by('-id')

    board_paginator = Paginator(memos, 6)
    page = request.GET.get('page')
    board_posts = board_paginator.get_page(page)
    return render(request,'board.html',{'memos' : memos, 'board_posts' : board_posts})

def index(request):
    user=request.user
    print('Request user : ', user.id)
    memos = Memo.objects.filter(user_id=user.id)
    current = memos.filter(directory=user.profile.currentdir)

    paginator = Paginator(current, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'index.html',{'memos' : memos, 'current' : current, 'userid' : user.id, 'posts' : posts})

def make_memo(request):
    user=request.user
    print(user.id)
    memo = Memo()
    memo.user_id = user.id
    memo.owner = user.username
    memo.keyword = request.POST['key']
    urls = request.POST['url']
    memo.pub_date = timezone.datetime.now()
    splited = urls.split('\n')
    memo.urls = urlScrap.scrapUrl(splited, memo.keyword)
    if len(memo.urls) > 1:
        memo.save()
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
    dirManagement.changedirname(user, dirname, newname)
    print(newname)
    return redirect('index')

def deletedir(request, dirname):
    user=request.user
    dname = dirname
    memos = Memo.objects.filter(user_id=user.id, directory=dirname)
    memos.delete()
    user.profile.currentdir='recently'
    user.profile.save()
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

def edit_memo(request, memo_id, keyword, urls):
    memo = Memo.objects.get(id=memo_id)
    splited_urls = urls.split(',')
    newline_urls = ''
    for i in range(0, len(splited_urls)):
        newline_urls += splited_urls[i] + '\n'
    memo.keyword = keyword
    memo.urls = newline_urls
    memo.save()
    return redirect('index')

def undo_share(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    memo.shared = False
    memo.save()
    return redirect('/')

def download_memo(request, memo_id):
    user=request.user
    newMemo = Memo()
    oldMemo = Memo.objects.get(id=memo_id)
    oldMemo.increaseDL()
    newMemo.user_id = user.id
    newMemo.owner = user.username
    newMemo.keyword = oldMemo.keyword
    newMemo.urls = oldMemo.urls
    newMemo.save()
    return redirect('index')

def movedir(request, memo_id, dirname):
    user = request.user
    memo = Memo.objects.get(id=memo_id)
    setattr(memo, 'directory', dirname)
    memo.save()
    return redirect('index')

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

def search(request):
    keyword = request.POST['searchBox']
    searched_memos = Memo.objects.filter(keyword= keyword, shared=True)
    print(keyword + " search!")
    return render(request,'search_board.html', {'searched_memos' : searched_memos})