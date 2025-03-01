from django.core.cache import cache
from config.settings import CACHE_ENABLED

from blogs.models import Publications

def get_publications_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст то получает из БД """
    if not CACHE_ENABLED:
        return Publications.objects.all()
    key = "publications_list"
    publications = cache.get(key)
    if publications is not None:
        return publications
    publications = Publications.objects.all()
    cache.set(key, publications, 60 * 15)
    return publications

