from django.contrib import admin

from reservation.models import *

admin.site.register(Reservation)
admin.site.register(Stylist)
admin.site.register(Review)
admin.site.register(Schedule)
admin.site.register(Service)
