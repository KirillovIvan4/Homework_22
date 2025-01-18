from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from online_store.models import Product, Category

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'category', 'purchase_price', 'preview']
    #template_name = 'product_form.html'
    success_url = reverse_lazy('online_store:product_list')

class ProductListView(ListView):
    model = Product
    #template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    #template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'category', 'purchase_price', 'preview']
    success_url = reverse_lazy('online_store:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    #template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('online_store:product_list')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("message")
        print(f"Имя - {name}\nПочта - {email}\nСообщение - {massage}")
        return HttpResponse(f"Спасибо {name}!")

    return render(request, 'online_store/contacts.html')

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    #template_name = 'product_form.html'
    success_url = reverse_lazy('online_store:category_list')

class CategoryListView(ListView):
    model = Category
    #template_name = 'product_list.html'
    context_object_name = 'category'

class CategoryDetailView(DetailView):
    model = Category
    #template_name = 'product_detail.html'
    context_object_name = 'category'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    success_url = reverse_lazy('online_store:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    #template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('online_store:category_list')

def category_product_detail(request, pk):
    category = Category.objects.get(pk=pk)
    products = category.product.all()
    return render(request, 'category_product_detail.html', {'category': category, 'products': products})