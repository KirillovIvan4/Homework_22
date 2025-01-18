from django.db import models


NULLBLE = {"blank": True, "null": True}

class Publications(models.Model):
    title = models.CharField(max_length=100, verbose_name="заголовок")
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to="products/", verbose_name="превью", **NULLBLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последних изменений")
    publication_flag = models.BooleanField(default=True, verbose_name="опубликовано")
    number_of_views = models.IntegerField(default=0, verbose_name="просмотры")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ["title", "created_at", "created_at", "updated_at", "number_of_views"]  # Сортировка
        db_table = 'Publications'  # Название таблици