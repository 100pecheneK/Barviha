from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('BritCat/', include('BritCat.urls')),
    # path('SibirCat', include('SibirCat.urls')),
]