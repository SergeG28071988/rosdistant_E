from django.contrib import admin

from .models import City, Country, Human

# Register your models here.


class CityAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


class HumanAdmin(admin.ModelAdmin):
    pass


admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Human, HumanAdmin)
