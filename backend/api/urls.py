from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/tumblr/(?P<name>[\w\-]+)/$', views.tumblr_lookup),
]