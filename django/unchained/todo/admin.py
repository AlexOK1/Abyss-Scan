from django.contrib import admin
from .models import Favorite, Manga

# Register your models here.
admin.site.register(Manga)
admin.site.register(Favorite)