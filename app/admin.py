from django.contrib import admin

from app.models import City, Street, Shop


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    list_filter = ('city',)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'street', 'house', 'opening_time', 'closing_time')
    list_filter = ('city',)
