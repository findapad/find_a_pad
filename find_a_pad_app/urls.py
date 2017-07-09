from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name='welcome'),
    url(r'^search/', views.search, name='search'),
    url(r'^location/', views.location, name='location')
]