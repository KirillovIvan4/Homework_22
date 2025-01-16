from django.urls import path
from . import views
from blogs.views import PublicationsCreateView, PublicationsUpdateView, PublicationsDeleteView, PublicationsListView, PublicationsDetailView
app_name = 'blogs'

urlpatterns = [
    path('publications/', PublicationsListView.as_view(), name='publications_list'),
    path('publications/<int:pk>/', PublicationsDetailView.as_view(), name='publications_detail'),
    path('publications/new/', PublicationsCreateView.as_view(), name='publications_create'),
    path('publications/<int:pk>/edit/', PublicationsUpdateView.as_view(), name='publications_edit'),
    path('publications/<int:pk>/delete/', PublicationsDeleteView.as_view(), name='publications_delete'),
]