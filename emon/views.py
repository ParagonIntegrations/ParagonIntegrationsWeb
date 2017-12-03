from django.shortcuts import render
#from django.views.generic.base import TemplateView
from django.views import generic
from .models import Installation, Meter, Channel, ChannelData

# Create your views here.

class Index(List):
    template_name = "index.html"


class InstallationListView():
