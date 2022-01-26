from django.contrib import admin

from movies.models import Movie, Video


# Register your models here.
class VideoInline(admin.StackedInline):
    model = Video


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
