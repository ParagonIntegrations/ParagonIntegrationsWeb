from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^installations$', views.InstallationListView.as_view(), name='installations'),
    url(r'^installation/(?P<pk>\d+)$', views.InstallationDetailView.as_view(), name='installation-detail'),
    url(r'^meters$', views.MeterListView.as_view(), name='meters'),
    url(r'^meter/(?P<pk>\d+)$', views.MeterDetailView.as_view(), name='meter-detail'),
    url(r'^channels$', views.ChannelListView.as_view(), name='meters'),
    url(r'^channel/(?P<sk>\d+)$', views.ChannelDetailView.as_view(), name='meter-detail'),
]