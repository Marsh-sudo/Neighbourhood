from django.urls.conf import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    re_path('^$',views.index,name='home'),
    re_path('^hood$',views.hoods,name='estates'),
    re_path('^my_estate/<int:id>$',views.estates,name='my_estate'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)