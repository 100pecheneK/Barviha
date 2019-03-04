from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='office-main'),
    path('list_1/', views.list_1, name='office-list_1'),
]
