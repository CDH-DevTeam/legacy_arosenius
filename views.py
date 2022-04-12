from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from . import models, serializers, schemas


class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = models.Artwork.objects.all()
    serializer_class = serializers.ArtworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    schema = schemas.MetaDataSchema()


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    schema = schemas.MetaDataSchema()

class KeywordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Keyword.objects.all()
    serializer_class = serializers.KeywordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    schema = schemas.MetaDataSchema()

class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    schema = schemas.MetaDataSchema()