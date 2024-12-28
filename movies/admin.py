from django.contrib import admin
from . models import Movie

@admin.register(Movie)
class MoviAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']