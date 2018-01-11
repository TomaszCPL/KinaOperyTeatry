from rest_framework import serializers
from map.models import Place,Shows


class ShowsSerializer(serializers.ModelSerializer):
    """Serializer for our user profile objects"""

    class Meta:
        model = Shows
        fields = ('title','date','time',)


class PlacesSerializer(serializers.ModelSerializer):
    """Serializer for our user profile objects"""
    shows = ShowsSerializer(many=True)

    class Meta:
        model = Place
        fields = ('name','lat','long','shows')