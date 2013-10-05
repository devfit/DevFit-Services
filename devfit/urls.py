from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devfit.views.home', name='home'),
    # url(r'^devfit/', include('devfit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^devfit/admin/', include(admin.site.urls)),
    
    url(r'^devfit/services/', include('models.urls')),
)
