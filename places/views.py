from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def index(request):
    features = []
    for place in Place.objects.all():
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': reverse('places', args=[place.pk])
            }
        })

    places = {
        'type': 'FeatureCollection',
        'features': features
    }
    context = {'places': places}
    return render(request, 'index.html', context)


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    serialized_place = {
        'title': place.title,
        'imgs': [img.content.url for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }

    return JsonResponse(serialized_place, json_dumps_params={'indent': 2, 'ensure_ascii': False})
