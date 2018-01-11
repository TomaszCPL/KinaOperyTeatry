from django.contrib import admin
from .models import Place
from .models import Shows

# Register your models here.

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(Shows)
class ShowsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'place')
    pass
