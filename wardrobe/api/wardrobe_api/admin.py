from django.contrib import admin
from .models import Location
from .models import Bin

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    pass
