from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^devfit/admin/', include(admin.site.urls)),
    
    url(r'^devfit/services/', include('models.urls')),
    url(r'^devfit/auth/', include('auth.urls')),
)
