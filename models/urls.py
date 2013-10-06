from views import LiftDataListCreateView, LiftDataRetrieveUpdateDestroy, LiftDataSearchView, LiftHistoryListCreateView, LiftSetListCreateView
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^liftdata/$', LiftDataListCreateView.as_view()),
    url(r'^liftdata/(?P<pk>[0-9]+)/$', LiftDataRetrieveUpdateDestroy.as_view()),
    url(r'^liftdata/filter/(?P<user>[0-9]+)/$', LiftDataSearchView.as_view()),
    
    url(r'^lifthistory/$', LiftHistoryListCreateView.as_view()),
    
    url(r'^liftset/$', LiftSetListCreateView.as_view()),
)

# urlpatterns = format_suffix_patterns(urlpatterns)
