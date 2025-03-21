import logging
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinValueValidator
from django.db import models
from online_store.models import Product, Category

ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    name = forms.CharField(validators=[MaxLengthValidator(100)])
    fields = ['name', 'description', 'preview', 'category', 'purchase_price']
    purchase_price = models.IntegerField(MinValueValidator(0, message='Test'))

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
