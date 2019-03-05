from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='barviha-home'),
    path('blog/', views.list_1, name='barviha-list_1'),
    path('list_2/', views.list_2, name='barviha-list_2'),
    path('list_3/', views.list_3, name='barviha-list_3'),
]
