from django.conf.urls import patterns, include, url

from .views import HttpRequestListView


urlpatterns = patterns(
    '',
   url(r'^$', HttpRequestListView.as_view()),

   )