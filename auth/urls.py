from auth.views.LoginView import LoginView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view()),
)
