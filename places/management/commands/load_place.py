from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from hashlib import md5
from urllib.request import urlopen
import requests

from places.models import Place, Image


def save_place(place):
    place_record, created = Place.objects.get_or_create(
        title=place['title'],
        defaults={
            'description_short': place.get('description_short', ''),
            'description_long': place.get('description_long', ''),
            'lat': place['coordinates']['lat'],
            'lng': place['coordinates']['lng'],
        }
    )

    if not created:
        return

    images = []
    for order, img_url in enumerate(place.get('imgs', [])):
        image_content = urlopen(img_url).read()
        content_file = ContentFile(image_content, name=md5(image_content).hexdigest())
        images.append(Image(place=place_record, content=content_file, order=order))

    Image.objects.bulk_create(images)


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
