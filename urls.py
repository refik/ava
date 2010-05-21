from django.conf.urls.defaults import *
from ava.settings import PROJECT_PATH
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^', include('ava.mainpage.urls')),    
	(r'^admin/', include(admin.site.urls)),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/media' % PROJECT_PATH}),
)
