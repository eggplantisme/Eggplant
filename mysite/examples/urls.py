from django.urls import path
from . import views


app_name='examples'
urlpatterns = [
    path('button/', views.button, name='button'),
    path('3d_video/', views.video_3d, name='3d_video'),
    path('loading/', views.loading, name='loading'),
]
