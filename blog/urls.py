from django.conf.urls import url
from . import views
urlPatterns=[
    url(r'^$', views.post_list, name='post_list'),
]