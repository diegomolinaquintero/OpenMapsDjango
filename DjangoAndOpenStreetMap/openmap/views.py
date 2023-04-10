import requests
from django.shortcuts import render
import osmapi


def osm_api(request):
    url = 'https://www.openstreetmap.org/api/0.6/relation/7154369/full'
    response = requests.get(url)
    data = response.text

    context = {'data': data}
    return render(request, 'osm_api.html', context)


def osm_map(request):
    api = osmapi.OsmApi()
    relation_id = 7154369
    data = api.RelationFull(relation_id)

    nodes = []
    ways = []
    relations = []

    for item in data:
        if item['type'] == 'node':
            nodes.append(item)
        elif item['type'] == 'way':
            ways.append(item)
        elif item['type'] == 'relation':
            relations.append(item)

    context = {
        'nodes': nodes,
        'ways': ways,
        'relations': relations,
    }

    return render(request, 'osm_map.html', context)
