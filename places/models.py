from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    description_short = models.TextField(verbose_name='Описание(краткое)', blank=True)
    description_long = HTMLField(verbose_name='Описание(полное)', blank=True)
    lng = models.FloatField(
        verbose_name='Долгота',
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    lat = models.FloatField(
        verbose_name='Широта',
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )

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
