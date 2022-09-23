from django.db import models
from .category import Category


class Product(models.Model):
    title = models.CharField('назваие продукта', max_length=20, unique=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(
        verbose_name='Дата публикации на сайте',
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.title} {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
