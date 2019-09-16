# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Works

# Creating your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class WorksList(ListView):
    model = Works
    template_name = 'works.html'
    context_object_name = 'works_list'
    
    def get_quesryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worklists'] = self.model.objects.all()
        
        return context