from django.contrib import admin
from . import models

@admin.register(models.Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Lyric)
class LyricAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    pass


