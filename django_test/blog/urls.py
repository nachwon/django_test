from django.conf.urls import url

from blog.views import blog_index, post_detail, post_create, post_delete

urlpatterns = [
    url(r'^$', blog_index, name='blog_index'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^post_create/$', post_create, name='post_create'),
    url(r'^post_delete/(?P<pk>\d+)/$', post_delete, name='post_delete'),
]