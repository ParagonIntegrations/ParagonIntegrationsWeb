from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Installations, Meters, Channels, ChannelData

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"


class InstallationListView(generic.ListView):
    model = Installations
    queryset = Installations.objects.order_by('id')


class InstallationDetailView(generic.DetailView):
    model = Installations


class MeterListView(generic.ListView):
    model = Meters
    queryset = Meters.objects.order_by('id')


class MeterDetailView(generic.DetailView):
    model = Meters

class ChannelListView(generic.ListView):
    model = Channels
    queryset = Channels.objects.order_by('id')


class ChannelDetailView(generic.DetailView):
    model = Channels