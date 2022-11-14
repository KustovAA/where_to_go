from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    description_short = models.CharField(max_length=500, verbose_name='Описание(краткое)')
    description_long = models.TextField(verbose_name='Описание(полное)')
    lng = models.CharField(max_length=200, verbose_name='Долгота')
    lat = models.CharField(max_length=200, verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    src = models.CharField(max_length=1000, verbose_name='Ссылка на картинку', null=True, blank=True)
    content = models.ImageField(verbose_name='Картинка', null=True)
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE,
        null=True
    )

    def get_url(self):
        try:
            return self.content.url
        except ValueError:
            return self.src
