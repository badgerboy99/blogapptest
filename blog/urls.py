from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^topfive/$', views.views_list),
    url(r'^post/new/$', views.new_post, name ='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post, name='edit'),
]