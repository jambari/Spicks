from django.contrib import admin
from .models import Station, Event, Arrival
# Register your models here.

admin.site.register(Station)
admin.site.register(Event)
admin.site.register(Arrival)
