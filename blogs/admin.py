
from django.contrib import admin
from blogs.models import Publications


@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'updated_at', 'publication_flag', 'number_of_views',)
    list_filter = ('updated_at', 'publication_flag')
    search_fields = ('title', 'content',)
