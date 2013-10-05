from views import LiftDataListView
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^$', LiftDataListView.as_view()),
    # url(r'^(?P<pk>[0-9]+)/$', CCCommonCoreView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
