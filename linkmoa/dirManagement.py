from django.contrib.auth.models import User
from django.contrib import auth
from django.forms.models import model_to_dict

def makeDirectory(user, name):
    if name=='': # blank input 예외처리
        return
    for dir, key in model_to_dict(user.profile).items():
        if key == name: # 중복된 이름 예외처리
            return 0
        if key == '':
            user.profile.increase()
            setattr(user.profile, dir, name)
            user.profile.save()
            break

# q

def deleteDirectory(user, name):
    k=0
    saveDir=""
    print(model_to_dict(user.profile).items())
    for dir, key in model_to_dict(user.profile).items():
        if key == name:
            user.profile.decrease()
            setattr(user.profile, dir, "")
            user.profile.save()
            saveDir = dir
            k=1
        if k == 1 and key != "":
            setattr(user.profile, saveDir, key)
            user.profile.save()
            saveDir = dir
        if saveDir != -1 and key == "":
            setattr(user.profile, saveDir, "")
            user.profile.save()
            saveDir = -1
    user.profile.currentdir='recently'
    user.profile.save()

def changedirname(user, old, new, dirmemo):
    for memo in dirmemo:
        memo.directory=new
        memo.save()

    for dir, value in model_to_dict(user.profile).items():
        if value == old:
            setattr(user.profile, dir, new)
            user.profile.save()
            break