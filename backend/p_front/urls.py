from django.urls import path, include

from .views import *

app_name = 'front'

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('about', AboutView.as_view(), name='about'),
    path('works', WorksListView.as_view(), name='works_lists'),
    path('works-details', WorksDetailView.as_view(), name='works_details'),
]