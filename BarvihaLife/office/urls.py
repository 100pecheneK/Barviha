from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^admin/$', views.admin, name='add_blog'),
    url(r'^edit/blog/(?P<id>\d+)/$', views.edit_blog, name='edit_blog'),
    url(r'^blog/(?P<id>\d+)/$', views.blog, name='blog'),  # < 1
    #path('', views.main, name='office-main'),
    #path('list_1/', views.list_1, name='office-list_1'),
]
