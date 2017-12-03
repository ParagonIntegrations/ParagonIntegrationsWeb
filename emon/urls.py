from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^installations/$', views.InstallationListView.as_view(), name='installations'),
    url(r'^installation/(?P<pk>\d+)/$', views.InstallationDetailView.as_view(), name='installation-detail'),
    url(r'^meters/$', views.MeterListView.as_view(), name='meters'),
    url(r'^meter/(?P<pk>\d+)/$', views.MeterDetailView.as_view(), name='meter-detail'),
    url(r'^channels/$', views.ChannelListView.as_view(), name='channel'),
    url(r'^channel/(?P<pk>\d+)/$', views.ChannelDetailView.as_view(), name='channel-detail'),
]