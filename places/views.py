from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Place


def index(request):
    template = loader.get_template('index.html')
    places = Place.objects.all()

    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": reverse('places', args=[place.pk])
            }
        })

    places = {
        "type": "FeatureCollection",
        "features": features
    }
    context = {'places': places}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def place(request, id):
    place = get_object_or_404(Place, pk=id)

    return JsonResponse({
        "title": place.title,
        "imgs": [img.get_url() for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    })
