from django.core.management.base import BaseCommand
from django.core.files import File
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
import requests

from places.models import Place, Image


def save_place(place):
    new_place, created = Place.objects.get_or_create(
        title=place['title'],
        defaults={
            'description_short': place['description_short'],
            'description_long': place['description_long'],
            'lat': place['coordinates']['lat'],
            'lng': place['coordinates']['lng'],
        }
    )

    for img_url in place['imgs']:
        image_record = Image(place=new_place)
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urlopen(img_url).read())
        img_temp.flush()
        image_record.content.save(img_url.split('/')[-1], File(img_temp))


class Command(BaseCommand):
    help = 'load new place'

    def handle(self, *args, **options):
        data_url = options['data_url']

        response = requests.get(data_url)
        response.raise_for_status()

        place = response.json()
        save_place(place)

    def add_arguments(self, parser):
        parser.add_argument('data_url', type=str)
