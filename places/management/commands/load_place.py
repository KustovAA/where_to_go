from django.core.management.base import BaseCommand
import requests

from places.models import Place, Image


def save_place(place):
    new_place, created = Place.objects.get_or_create(
        title=place['title'],
        description_short=place['description_short'],
        description_long=place['description_long'],
        lat=place['coordinates']['lat'],
        lng=place['coordinates']['lng']
    )
    Image.objects.bulk_create([Image(src=img, place=new_place) for img in place['imgs']])


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
