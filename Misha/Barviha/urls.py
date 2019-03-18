from django.urls import path, include
from Barviha import views

urlpatterns = (
    path('', views.start, name='start'),
)
