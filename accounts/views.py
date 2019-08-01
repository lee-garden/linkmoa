from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print(user.username + " login")
            return redirect('/',user)
        else:
            return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_user(
                request.POST['username'],
                password = request.POST['password']
            )
        auth.login(request,user)
        return redirect('/')
    return render(request,'signup.html')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print('log out success')
        return redirect('/')
    return render(request,'login.html')