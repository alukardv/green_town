from django.shortcuts import render
from django.views.generic import TemplateView
import json
from django.core.serializers import serialize
from apps.markers.models import Marker


class MarkersMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        markers = Marker.objects.using('markers_db').all()
        context["markers"] = json.loads(serialize("geojson", markers))
        return context
