from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create', views.create, name = 'create'),
    url(r'^(?P<id>\d+)/add', views.add, name = 'add'),
    url(r'^(?P<id>\d+)$', views.show, name = 'show'),
    url(r'^(?P<id>\d+)/remove', views.remove, name = 'remove'),
    url(r'^(?P<id>\d+)/delete', views.delete, name = 'delete'),
    url(r'^logout', views.logout, name = 'logout')
]