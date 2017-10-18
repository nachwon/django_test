from django.conf.urls import url

from blog.views import blog_index, post_detail, post_create

urlpatterns = [
    url(r'^$', blog_index, name='blog_index'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='detail_view'),
    url(r'^post_create/$', post_create, name='post_create')
]