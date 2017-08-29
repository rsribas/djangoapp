#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^support/$', views.support_topics, name='support_topics'),
    url(r'^new_support/$', views.support_new, name='support_new'),
    url(r'^devices/$', views.devices, name='devices'),
]
