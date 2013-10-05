from views import LiftDataListCreateView, LiftDataRetrieveUpdateDestroy, LiftDataSearchView
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^$', LiftDataListCreateView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', LiftDataRetrieveUpdateDestroy.as_view()),
    
    url(r'^filter/(?P<user>[0-9]+)', LiftDataSearchView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
