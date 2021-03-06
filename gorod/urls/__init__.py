"""
    Base gorod urls
"""

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from gorod.views import base, user, complaint
from gorod.utils.sitemap import sitemaps

from django.contrib.flatpages import views as flatpages_views


urlpatterns = patterns('',
    # Project main page
    url(r'^$', base.IndexView.as_view(), name='index'),

    # User profile
    url(r'^logout/?$', user.LogoutView.as_view(), name='logout'),
    url(r'^login/?$', user.LoginView.as_view(), name='login'),

    # Captcha
    url(r'^captcha/', include('captcha.urls')),

    # Comments
    #url(r'^comments/add/?', CommentsAddView.as_view(), name='comments-add'),
    url(r'^comments/', include('comments.urls')),

    # Likes
    url(r'^likes/', include('likes.urls', namespace='likes')),

    ## API urls
    url(r'^api/', include('gorod.urls.api', namespace='gorodapi')),

    # Sitemap.xml
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, name='sitemap'),


    ## Static pages
    #url(r'^license/?', TemplateView.as_view(template_name="gorod/rules.html"), name='rules'),
    url(r'(?P<url>license)/?$', flatpages_views.flatpage, {'url': '/license/'}, name='license'),
    url(r'(?P<url>help)/?$', flatpages_views.flatpage, {'url': '/help/'}, name='help'),

    # Complaint add
    url(r'^complaint/?', complaint.ComplaintAddView.as_view(), name='complaint'),

    # Old User redirects
    url(r'^user/(?P<user_id>\d+)/?', user.OldUserRedirectView.as_view(), name='old-user'),

    # One City pages
    url(r'^(?P<city_name>\w+)/', include('gorod.urls.city', namespace='gorod')),
)

