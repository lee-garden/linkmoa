from django.shortcuts import render, redirect
from testapp import urlScrap
from .models import Memo

# Create your views here.
def index(request):
    memos = Memo.objects
    print('open page')
    return render(request,'index.html',{'memos' : memos})

def make_memo(request):
    memo = Memo()
    memo.user_id = 1
    memo.keyword = request.POST['key']
    urls = request.POST['url']
    splited = urls.split('\n')
    memo.urls = urlScrap.scrapUrl(splited, memo.keyword)
    if len(memo.urls) > 1:
        memo.save()
    return redirect('/')