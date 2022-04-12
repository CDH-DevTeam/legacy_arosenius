# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

def get_fields(model: models.Model, exclude=['id']):
    return [field.name for field in model._meta.fields if field.name not in exclude]

class Artwork(models.Model):
    insert_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=20, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    deleted = models.IntegerField()
    published = models.IntegerField()
    museum_int_id = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    museum = models.CharField(max_length=100, blank=True, null=True)
    museum_url = models.CharField(max_length=300, blank=True, null=True)
    date_human = models.CharField(max_length=20, blank=True, null=True)
    date = models.CharField(max_length=10, blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True)
    technique_material = models.CharField(max_length=200, blank=True, null=True)
    acquisition = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    inscription = models.TextField(blank=True, null=True)
    material = models.CharField(max_length=300, blank=True, null=True)
    creator = models.CharField(max_length=100, blank=True, null=True)
    signature = models.CharField(max_length=200, blank=True, null=True)
    sender = models.ForeignKey('arosenius.Person', models.DO_NOTHING, db_column='sender', blank=True, null=True, related_name='related_sender')
    recipient = models.ForeignKey('arosenius.Person', models.DO_NOTHING, db_column='recipient', blank=True, null=True, related_name='related_recipient')
    exhibitions = models.CharField(max_length=300, blank=True, null=True)
    literature = models.CharField(max_length=300, blank=True, null=True)
    reproductions = models.CharField(max_length=300, blank=True, null=True)
    bundle = models.CharField(max_length=50, blank=True, null=True)
    bundle_order = models.PositiveIntegerField(blank=True, null=True)
    bundle_side = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artwork'


class Image(models.Model):
    artwork = models.ForeignKey(Artwork, models.DO_NOTHING, db_column='artwork')
    filename = models.CharField(max_length=100)
    type = models.CharField(max_length=10, blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    page = models.IntegerField(blank=True, null=True)
    pageid = models.CharField(max_length=20, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    side = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'
        unique_together = (('artwork', 'filename'),)


class Keyword(models.Model):
    artwork = models.ForeignKey(Artwork, models.DO_NOTHING, db_column='artwork')
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'keyword'
        unique_together = (('artwork', 'type', 'name'),)


class Person(models.Model):
    name = models.CharField(unique=True, max_length=200)
    birth_year = models.CharField(max_length=4, blank=True, null=True)
    death_year = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'
