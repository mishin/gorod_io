""" Base gorod urls """

from django.conf.urls import patterns, include, url

from gorod.views import base


urlpatterns = patterns('',
    # One City pages
    url(r'^town/(?P<city_name>\w+)/', include('gorod.urls.city', namespace='gorod')),

    # Main gorod.io page
    url(r'^$', base.index, name='index')
)
