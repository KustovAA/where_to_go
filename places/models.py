from django.db import models


class Image(models.Model):
    src = models.CharField(max_length=1000, verbose_name='Ссылка на картинку', null=True, blank=True)
    content = models.ImageField(verbose_name='Картинка', null=True)

    def get_url(self):
        return self.content if self.content else self.src


class Place(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    images = models.ManyToManyField(Image, verbose_name='Изображения', related_name='images')
    description_short = models.CharField(max_length=500, verbose_name='Описание(краткое)')
    description_long = models.TextField(verbose_name='Описание(полное)')
    lng = models.IntegerField(verbose_name='Долгота')
    lat = models.IntegerField(verbose_name='Широта')

    def __str__(self):
        return self.title
