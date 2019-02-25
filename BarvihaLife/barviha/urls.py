from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='barviha-home'),
    path('list/', views.list_1, name='barviha-list_1'),
]
