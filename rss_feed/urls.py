from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^search-form', views.feed, name = 'feed'),
    url(r'^search', views.search, name = 'search'),
    url(r'^get', views.get, name = 'get'),

]