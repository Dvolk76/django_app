from django.contrib import admin
from . import models
# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
        'created',
        'updated'
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'city',
        'street',
        'building_number',
        'block'
    ]

admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.City, CityAdmin)