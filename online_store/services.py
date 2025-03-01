from django.core.cache import cache
from config.settings import CACHE_ENABLED
from online_store.models import Product, Category

def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст то получает из БД """
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products, 60 * 15)
    return products

def get_categorys_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст то получает из БД """
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "category_list"
    categorys = cache.get(key)
    if categorys is not None:
        return categorys
    categorys = Category.objects.all()
    cache.set(key, categorys, 60 * 15)
    return categorys

def get_products_by_category(category_id):

    if not CACHE_ENABLED:
        return Product.objects.filter(category=Category.objects.get(pk=category_id))
    key = f'products_by_category_{category_id}'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(category=Category.objects.get(pk=category_id))
    cache.set(key, products, 60)
    return products