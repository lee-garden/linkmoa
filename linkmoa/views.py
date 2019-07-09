from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from linkmoa import urlScrap
from accounts import views
from .models import Memo

# Create your views here.
def board(request):
    return render(request,'board.html')

def index(request):
    user=request.user
    print(user.id)
    memos = Memo.objects.filter(user_id=user.id)
    print('open page')
    return render(request,'index.html',{'memos' : memos, 'userid' : user.id})

def make_memo(request):
    user=request.user
    print(user.id)
    memo = Memo()
    memo.user_id = user.id
    memo.keyword = request.POST['key']
    urls = request.POST['url']
    splited = urls.split('\n')
    memo.urls = urlScrap.scrapUrl(splited, memo.keyword)
    if len(memo.urls) > 1:
        memo.save()
    return redirect('index')

def delete_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    memo.delete()
    return redirect('index')