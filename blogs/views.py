from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from blogs.models import Publications
from blogs.services import get_publications_from_cache


class PublicationsCreateView(LoginRequiredMixin, CreateView):
    model = Publications
    fields = ['title', 'content', 'preview', 'publication_flag']
    #template_name = 'Publications_form.html'
    success_url = reverse_lazy('blogs:publications_list')

    def form_valid(self, form):
        publication = form.save()
        user = self.request.user
        publication.creator = user
        publication.save()
        return super().form_valid(form)


@method_decorator(cache_page(60 * 15), name='dispatch')
class PublicationsListView(ListView):
    model = Publications
    #template_name = 'Publications_list.html'
    context_object_name = 'publications'

    # def get_queryset(self):
    #     return Publications.objects.filter(publication_flag=True)
    # def get_queryset(self):
    #     return get_publications_from_cache()

    def get_queryset(self):
        return Publications.objects.filter(publication_flag=True)
        # return get_publications_from_cache()


@method_decorator(cache_page(60 * 15), name='dispatch')
class PublicationsDetailView(DetailView):
    model = Publications
    #template_name = 'Publications_detail.html'
    context_object_name = 'publications'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object

class PublicationsUpdateView(LoginRequiredMixin, UpdateView):
    model = Publications
    fields = ['title', 'content', 'preview', 'publication_flag']
    success_url = reverse_lazy('blogs:publications_list')

    def get_success_url(self):
        return reverse('blogs:publications_detail', args=[self.kwargs.get('pk')])

class PublicationsDeleteView(DeleteView):
    model = Publications
    #template_name = 'Publications_confirm_delete.html'
    success_url = reverse_lazy('blogs:publications_list')