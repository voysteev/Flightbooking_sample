from django.contrib import admin
from .models import airports, Flight, Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = ('id','origin','destination','duration')

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',) #----> to show many to many field with a better interface, flights is the many to many field in Passenger model, dont forget the comma
    
# Register your models here.
admin.site.register(airports)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger,PassengerAdmin)
