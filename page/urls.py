from django.conf.urls import patterns, url

urlpatterns = patterns('page.views', 
	url(r'^$', 'index'),

)
