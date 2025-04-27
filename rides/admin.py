from django.contrib import admin
from .models import Rider, Driver, Vehicle, Ride , Payment

admin.site.register(Rider)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Ride)
admin.site.register(Payment)
