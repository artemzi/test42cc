from django.conf.urls import patterns, include, url

from .views import HomePersonListView


urlpatterns = patterns(
    '',
   url(r'^$', HomePersonListView.as_view(), name="person-detail"),

   )