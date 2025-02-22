import logging
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinValueValidator
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from online_store.models import Product, Category


ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
# logger = logging.getLogger(__name__)
# @login_required
# def create_product(request):
#     print(f"Текущий пользователь: {request.user}")
#     print(f"ID пользователя: {request.user.id}")
#     print(f"Аутентифицирован ли пользователь: {request.user.is_authenticated}")
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             if request.user.is_authenticated:
#                 product.creator = request.user
#             else:
#                 return redirect('users:login')
#             product.save()
#             return redirect('online_store:product_list')
#         else:
#             form = ProductForm()
#         return render(request,'product_form.html' ,{'form':form})

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name,  field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    name = forms.CharField(validators=[MaxLengthValidator(100)])
    fields = ['name', 'description', 'preview', 'category', 'purchase_price']
    purchase_price = models.IntegerField(MinValueValidator(0,message='Test'))

    # @login_required
    # def create_product(request):
    #     print(f"Текущий пользователь: {request.user}")
    #     print(f"ID пользователя: {request.user.id}")
    #     print(f"Аутентифицирован ли пользователь: {request.user.is_authenticated}")
    #     if request.method == "POST":
    #         form = ProductForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             product = form.save(commit=False)
    #             if request.user.is_authenticated:
    #                 product.creator = request.user
    #             else:
    #                 return redirect('users:login')
    #             product.save()
    #             return redirect('online_store:product_list')
    #         else:
    #             form = ProductForm()
    #         return render(request, 'product_form.html', {'form': form})

    class Meta:
        model = Product
        fields = ['name', 'description', 'preview', 'category', 'purchase_price']

    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        for word in ban_list:
            if word in name.lower():
                raise ValidationError(f"В названии продукта нельзя использовать запрещенные слово {word}.")
        return name


    def clean_description(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        for word in ban_list:
            if word in description.lower():
                raise ValidationError(f"В описании продукта нельзя использовать запрещенные слово {word}.")
        return description

