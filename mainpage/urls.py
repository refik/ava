from django.conf.urls.defaults import *

urlpatterns = patterns('ava.mainpage.views',
	(r'^$','index'),
	(r'^page(?P<pagination_id>[0-9]+)/$', 'index'),
	(r'^comment/$', 'comment'),
	(r'^(?P<comment_id>\d+)/(?P<pm>\d+)/like/$', 'like'),
)
