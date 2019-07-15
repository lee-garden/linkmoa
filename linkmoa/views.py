from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from linkmoa import urlScrap
from linkmoa import dirManagement
from accounts import views
from .models import Memo
from .models import Profile

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

def deletedir(request, dirname):
    user=request.user
    dname = dirname
    memos = Memo.objects.filter(user_id=user.id, directory=dirname)
    memos.delete()
    dirManagement.deleteDirectory(user, dname)
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

def edit_memo(request, memo_id, keyword, urls):

    memo = Memo.objects.get(id=memo_id)

    print('id: ', memo_id, '\n')
    print('keyword: ', keyword, '\n')
    print('urls: ', urls, '\n')
    
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

def movedir(request, dirname):
    user = request.user
    memo = Memo.objects.get(id=user.profile.selectedMemo)
    a = request.POST.get('memo_id')
    print(a)
    print(dirname,'called')
    setattr(memo, 'directory', dirname)
    memo.save()
    return redirect('index')

def appear_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    memo.display='visible'
    memo.save()    
    return redirect('index')

def disappear_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    memo.display='invisible'
    memo.save()
    return redirect('index')

def search(request):
    keyword = request.POST['searchBox']
    searched_memos = Memo.objects.filter(keyword= keyword)
    print(keyword + " search!")
    return render(request,'search_board.html', {'searched_memos' : searched_memos})
