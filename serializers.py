from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from . import models

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artwork
        fields = '__all__'
        depth = 1


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'
        depth = 1

class KeywordSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Keyword
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'
        depth = 1
