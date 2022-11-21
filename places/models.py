from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    description_short = models.TextField(verbose_name='Описание(краткое)', blank=True)
    description_long = HTMLField(verbose_name='Описание(полное)', blank=True)
    lng = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Долгота')
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    content = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE,
        null=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
