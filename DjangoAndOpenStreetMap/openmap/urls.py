from django.urls import path
from .views import osm_api, osm_map

urlpatterns = [
    path('osm_api/', osm_api, name='osm_api'),
    path('osm_map/', osm_map, name='osm_map'),
]
