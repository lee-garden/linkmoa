from django.contrib.auth.models import User
from django.contrib import auth
from django.forms.models import model_to_dict

def makeDirectory(user, name):
    if key=='': 
        return
    for dir, key in model_to_dict(user.profile).items():
        if key == name:
            return 0
        if key == '':
            user.profile.increase()
            setattr(user.profile, dir, name)
            user.profile.save()
            break

def deleteDirectory(user, name):
    print(model_to_dict(user.profile).items())
    for dir, key in model_to_dict(user.profile).items():
        if key == name:
            user.profile.decrease()
            setattr(user.profile, dir, "")
            user.profile.save()
            break

def changedirname(user, old, new, dirmemo):
    for memo in dirmemo:
        memo.directory=new
        memo.save()

    for dir, value in model_to_dict(user.profile).items():
        if value == old:
            print(value)
            print(old)
            setattr(user.profile, dir, new)
            user.profile.save()
            print(new)
            break
