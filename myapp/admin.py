from django.contrib import admin
from .models import Genre, Developer, Game, Rating

# Register your models here.

admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Game)
admin.site.register(Rating)
