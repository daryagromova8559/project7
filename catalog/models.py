from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименованик')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/photo', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version = models.CharField(verbose_name='Версия')
    number_version = models.IntegerField(verbose_name='Номер версии')
    current_version = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.number_version}'