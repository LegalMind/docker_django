from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index_detail,name='index'),
	url(r'^postlist$',views.post_list,name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail,name='post_detail'),
	url(r'^portpolio$',views.portpolio_list,name='portpolio_list'),
	url(r'^sites$',views.sites,name='sites'),
]
