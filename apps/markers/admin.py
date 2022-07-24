from django.contrib import admin

from django.contrib.gis import admin
from apps.markers.models import Marker
from leaflet.admin import LeafletGeoAdmin

@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    list_display = ("name", "location")
