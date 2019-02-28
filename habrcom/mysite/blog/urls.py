from django.contrib import admin
from django.urls import path, re_path
from blog.views import PostsListView, PostDetailView

# функция автоматического обнаружения файлов admin.py в наших приложениях
admin.autodiscover()

urlpatterns = [
    # будет выводиться список постов
    path('', PostsListView.as_view(), name='list'),
    # будет выводиться пост с определенным номером
    re_path(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),

]
