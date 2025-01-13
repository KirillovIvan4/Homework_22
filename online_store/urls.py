from django.urls import path
from . import views
from online_store.views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView, ProductDetailView
app_name = 'online_store'

urlpatterns = [

    path('contacts', views.contacts, name='contacts'),


    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]