from django.urls import path
from django.conf.urls import url
from blog.feed import AllPostsRssFeed
from . import view

app_name = 'blog'
urlpatterns = [
    url(r"^$", view.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', view.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', view.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)$', view.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', view.TagView.as_view(), name='tag'),
    url(r'^rss/$', AllPostsRssFeed(), name='rss')
]
