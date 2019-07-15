from django.template import Library
from .. import models

register = Library()

@register.simple_tag
def setSelectedMemo(profile, id):
    setattr(profile, 'selectedMemo', id)
    print('setSelected : ', id)
    profile.save()