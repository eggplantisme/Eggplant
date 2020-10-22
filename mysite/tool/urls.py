from django.conf.urls import url
from . import view

app_name = 'tool'
urlpatterns = [
    url('^$', view.tool, name='tool')
]