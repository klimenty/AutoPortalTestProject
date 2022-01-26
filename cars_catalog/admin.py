from django.contrib import admin
# Added import
from .models import CarConfiguration, CarInstance, Manufacturer, CarModel, CarColor, Dealer, DealerCenter


class CarConfigurationAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'car_model', 'car_color')


class CarInstanceAdmin(admin.ModelAdmin):
    list_filter = ('vin', 'car_configuration', 'dealer', 'date_of_arrival_to_dealer', 'dealer_center',
                   'date_of_arrival_to_dealer_center')

    fieldsets = (
        ('Car Info', {
            'fields': ('vin', 'car_configuration')
        }),
        ('Dealer Info', {
            'fields': ('dealer', 'date_of_arrival_to_dealer', 'dealer_center', 'date_of_arrival_to_dealer_center')
        })
    )


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('manufacturer_name',)


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_model_name',)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_name',)


# Register your models here.
admin.site.register(CarConfiguration, CarConfigurationAdmin)
admin.site.register(CarInstance, CarInstanceAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarColor, ColorAdmin)
admin.site.register(Dealer)
admin.site.register(DealerCenter)
