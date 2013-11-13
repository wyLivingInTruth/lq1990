from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lq1990.views.home', name='home'),
    # url(r'^lq1990/', include('lq1990.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

	url(r'^admin/', include(admin.site.urls)),
    
	url(r'^page/', include('page.urls')),
    
	url(r'^$', 'lq1990.views.home', name='home'),
	
	url(r'^upload$', 'lq1990.views.upload'), 

	url(r'^articles$', 'lq1990.views.articles'),
)
