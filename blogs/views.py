from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
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

    def get_queryset(self):
        return Publications.objects.filter(publication_flag=True)

class PublicationsDetailView(DetailView):
    model = Publications
    #template_name = 'Publications_detail.html'
    context_object_name = 'publications'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object

class PublicationsUpdateView(UpdateView):
    model = Publications
    fields = ['title', 'content', 'preview', 'publication_flag']
    success_url = reverse_lazy('blogs:publications_list')

    def get_success_url(self):
        return reverse('blogs:publications_detail', args=[self.kwargs.get('pk')])

class PublicationsDeleteView(DeleteView):
    model = Publications
    #template_name = 'Publications_confirm_delete.html'
    success_url = reverse_lazy('blogs:publications_list')