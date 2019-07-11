from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from linkmoa import urlScrap
from linkmoa import dirManagement
from accounts import views
from .models import Memo
from. models import Profile

# Create your views here.
def board(request):
    user=request.user
    memos = Memo.objects.filter(shared=True)
    return render(request,'board.html',{'memos' : memos})

def index(request):
    user=request.user
    print('current user : ', user.id)
    memos = Memo.objects.filter(user_id=user.id)
    return render(request,'index.html',{'memos' : memos, 'userid' : user.id})

def make_memo(request):
    user=request.user
    print(user.id)
    memo = Memo()
    memo.user_id = user.id
    memo.owner = user.username
    memo.keyword = request.POST['key']
    urls = request.POST['url']
    splited = urls.split('\n')
    memo.urls = urlScrap.scrapUrl(splited, memo.keyword)
    if len(memo.urls) > 1:
        memo.save()
    return redirect('index')

def mkdir(request):
    user=request.user
    dname = request.POST['dirname']
    dirManagement.makeDirectory(user,dname)
    return redirect('index')

def delete_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    memo.delete()
    return redirect('index')

def share_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    memo.shared = True
    memo.save()
    return redirect('index')