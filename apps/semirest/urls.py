from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^products$', views.index),
    url(r'^products/show/(?P<id>\d+)$', views.show),
    url(r'^products/new$', views.new),
    url(r'^product/create$', views.create),
    url(r'^product/edit/(?P<id>\d+)$', views.edit),
    url(r'^product/(?P<id>\d+)/update$', views.update),
    url(r'^product/(?P<id>\d+)/destroy$', views.destroy),
]
