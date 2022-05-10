# from django.contrib import admin
from django.contrib.gis.db import models
from .models import *
from django.utils.html import format_html
from django.contrib.gis import admin

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Image)
class ImageModel(admin.ModelAdmin):
    fields = get_fields(Image)
    autocomplete_fields = ['artwork']
    #.append('image_preview')
    # readonly_fields = ('image_preview',)
    # list_display = ('bild', 'thumbnail_preview')

    # def image_preview(self, obj):
    #     return format_html(f'<img src="https://img.dh.gu.se/art/pyr/{obj.bild}.tif/full/full/0/default.jpg" height="300" />')

    # def thumbnail_preview(self, obj):
    #     return format_html(f'<img src="https://img.dh.gu.se/art/pyr/{obj.bild}.tif/full/full/0/default.jpg" height="100" />')


    # image_preview.short_description = 'Image preview'
    # image_preview.allow_tags = True
    # thumbnail_preview.short_description = 'Image thumbnail'
    # thumbnail_preview.allow_tags = True

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    fields = get_fields(Artwork)
    inlines = [ImageInline]
    search_fields = ['title', 'id']
    autocomplete_fields = ['sender', 'recipient']

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    fields = get_fields(Keyword) 
    list_display = get_fields(Keyword)
    search_fields = ['type', 'name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin): 
    fields = get_fields(Person) 
    list_display = get_fields(Person)
    search_fields = ['name']
