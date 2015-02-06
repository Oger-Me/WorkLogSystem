import django
from django.conf.urls import patterns, include, url

from WorkLog.Controllers.IndexController import *
from WorkLog.Controllers.CategoryController import *
from WorkLog.Controllers.TraceController import *

from django.contrib import admin
from WorkLogSystem import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WorkLogSystem.Views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', index),
    url(r'^api/worklog/?$', worklog),
    url(r'^api/worklog/category/?$', get_category),

    url(r'^debug/?$', debug),
    url(r'^resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIRS[0]}),
)