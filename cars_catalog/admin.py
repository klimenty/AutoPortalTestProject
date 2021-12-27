from django.contrib import admin
#Added import
from .models import Car, CarInstance, Manufacturer, CarModel, CarColor, Dealer, DealerCenter

# Register your models here.
admin.site.register(Car)
admin.site.register(CarInstance)
admin.site.register(Manufacturer)
admin.site.register(CarModel)
admin.site.register(CarColor)
admin.site.register(Dealer)
admin.site.register(DealerCenter)
