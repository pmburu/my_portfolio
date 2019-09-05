# from django.shortcuts import render
from django.views.generic import TemplateView

# Creating your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'