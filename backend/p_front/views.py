# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.http import Http404, HttpResponseRedirect
from .models import Works

# Creating your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class WorksListView(ListView):
    model = Works
    template_name = 'works.html'
    context_object_name = 'works_list'
    
    def get_quesryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worklists'] = self.model.objects.all()
        
        return context


class WorksDetailView(DetailView):
    model = Works
    template_name = 'work-details.html'
    context_object_name = 'works_details'
    slug_field = 'role'
    slug_url_kwarg = 'role'
    
    def get_queryset(self):
        return self.model.objects.filter(is_published=True)