from django.urls.conf import re_path,path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    re_path('^$',views.index,name='home'),
    re_path('^hood$',views.hoods,name='estates'),
    path('my_estate/<int:id>',views.estates,name='my_estate'),
    path('new_business/<int:id>',views.new_business,name='new_business'),
    path('new_post/<int:id>',views.new_post,name='new_post'),
    re_path('^newbusiness/<int:id>$',views.new_business,name='newbusiness'),
    re_path('^profiles$',views.profile,name='profile'),
    re_path('^leave_hood$',views.leave_hood,name='leave_hood'),
    re_path('^search$',views.search_hood,name='search'),
    re_path('^new_profile$',views.new_profile,name='new_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)