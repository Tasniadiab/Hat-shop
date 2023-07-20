from django.contrib import admin
from .models import Location

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
from .models import Bin


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    pass
