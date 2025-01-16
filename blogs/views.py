from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blogs.models import Publications

class PublicationsCreateView(CreateView):
    model = Publications
    fields = ['title', 'content', 'preview', 'publication_flag']
    #template_name = 'Publications_form.html'
    success_url = reverse_lazy('blogs:publications_list')

class PublicationsListView(ListView):
    model = Publications
    #template_name = 'Publications_list.html'
    context_object_name = 'publications'

class PublicationsDetailView(DetailView):
    model = Publications
    #template_name = 'Publications_detail.html'
    context_object_name = 'publications'

class PublicationsUpdateView(UpdateView):
    model = Publications
    fields = ['title', 'content', 'preview', 'publication_flag']
    success_url = reverse_lazy('blogs:publications_list')

class PublicationsDeleteView(DeleteView):
    model = Publications
    #template_name = 'Publications_confirm_delete.html'
    success_url = reverse_lazy('blogs:publications_list')