from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    description_short = models.TextField(verbose_name='Описание(краткое)', null=True, blank=True)
    description_long = HTMLField(verbose_name='Описание(полное)', null=True, blank=True)
    lng = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Долгота')
    lat = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    src = models.CharField(max_length=1000, verbose_name='Ссылка на картинку', null=True, blank=True)
    content = models.ImageField(verbose_name='Картинка', null=True, blank=True)
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE,
        null=True
    )

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def get_url(self):
        try:
            return self.content.url
        except ValueError:
            return self.src

    class Meta:
        ordering = ['order']
