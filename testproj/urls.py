from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
import linkmoa.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',linkmoa.views.board, name='board'),
    path('index/', linkmoa.views.index, name='index'),
    path('make_memo',linkmoa.views.make_memo, name='make_memo'),
    path('delete_memo/<int:memo_id>/', linkmoa.views.delete_memo, name='delete_memo'),
    path('share_memo/<int:memo_id>/', linkmoa.views.share_memo, name='share_memo'),
    path('undo_share/<int:memo_id>', linkmoa.views.undo_share, name='undo_share'),
    path('download_memo/<int:memo_id>', linkmoa.views.download_memo, name="download_memo"),
    # path('appear_memo/<int:memo_id>', linkmoa.views.appear_memo, name="appear_memo"),
    # path('disappear_memo/<int:memo_id>', linkmoa.views.disappear_memo, name="disappear_memo"),
    path('mkdir', linkmoa.views.mkdir, name='mkdir'),
    path('changedir/<cddir>', linkmoa.views.changedir, name='changedir'),
    path('changedirname/<dirname>', linkmoa.views.changedirname, name='changedirname'),
    re_path(r'^movedir/(?P<memo_id>\d+)/(?P<dirname>.*)/$',linkmoa.views.movedir, name='movedir'),
    path('deletedir/<dirname>', linkmoa.views.deletedir, name='deletedir'),
    path('search_board/', linkmoa.views.search, name='search_board'),
    path('tag_board/<tag>/', linkmoa.views.tag_board, name='tag_board'),
    re_path(r'^edit_memo/(?P<memo_id>\d+)/$', linkmoa.views.edit_memo, name='edit_memo'),

    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('signup/', accounts.views.signup, name='signup'),
]
