from django.contrib import admin
from .models import Room, Rent, District, Сategories

admin.site.site_header = 'wenzel administration'


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
	list_filter = ('name', 'created_at', 'price',)


class RentAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
	list_filter = ('name', 'created_at', 'price',)


admin.site.register(Rent, RentAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(District)
admin.site.register(Сategories)
