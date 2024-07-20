from django.db import models


NULLABLE = {'blank': True, 'null': True}


class City(models.Model):
    """ Класс представления модели City """
    name = models.CharField(max_length=100, verbose_name='Название города')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name',)


class Street(models.Model):
    """ Класс представления модели Street """
    name = models.CharField(max_length=100, verbose_name='Название улицы')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        ordering = ('name',)


class Shop(models.Model):
    """ Класс представления модели Shop """
    name = models.CharField(max_length=100, verbose_name='Название магазина')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name='Улица')
    house = models.PositiveSmallIntegerField(verbose_name='Дом')
    opening_time = models.TimeField(verbose_name="Время открытия")
    closing_time = models.TimeField(verbose_name="Время закрытия")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ('name',)
