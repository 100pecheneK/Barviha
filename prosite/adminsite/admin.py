from django.contrib import admin
from .models import Room

admin.site.site_header = 'wenzel administration'


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
	list_display = ('name',  'price', 'old_price', 'created_at', 'updated_at',)
	list_filter = ('name', 'created_at', 'price',)


admin.site.register(Room, RoomAdmin)
