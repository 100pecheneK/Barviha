from django.urls import path
from the_main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.test, name='the_main-test'),
    path('home', views.home, name='the_main-home'),
    path('contacti', views.contacti, name='the_main-contacti'),
    path('site', views.site, name='the_main-site'),
]

