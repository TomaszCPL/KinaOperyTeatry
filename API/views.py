from rest_framework import viewsets
from .serializers import PlacesSerializer
from map.models import Place


# Create your views here.

class PlacesViewSet(viewsets.ModelViewSet):
    serializer_class = PlacesSerializer
    queryset = Place.objects.all()






