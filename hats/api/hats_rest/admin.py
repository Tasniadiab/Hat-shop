from django.contrib import admin
from .models import Hats, LocationVO

# Register your models here.

@admin.register(LocationVO)
class LocationVOAdmin(admin.ModelAdmin):
    pass
@admin.register(Hats)
class HatsAdmin(admin.ModelAdmin):
    pass
