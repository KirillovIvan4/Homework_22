from django.urls import path
from . import views
from online_store.views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView, ProductDetailView
from online_store.views import CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CategoryListView, CategoryDetailView
app_name = 'online_store'

urlpatterns = [
    path('contacts', views.contacts, name='contacts'),

    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]