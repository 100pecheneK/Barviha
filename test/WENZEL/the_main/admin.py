from django.contrib import admin
from .models import *



class SubscribersAdmin (admin.ModelAdmin):
    list_display = ("first_name", "last_name",) #"email" список
    list_filter = ("first_name",) # фильтр по имени 
    #list_display = (field.name for field in Subscribers._meta.fields)
    fields = ("email",) # показывать только email
    #exclude = ("email",)
    search_fields = ("first_name", "email") #поиск по ...
    class Meta:
        model = Subscribers

admin.site.register(Subscribers, SubscribersAdmin)
admin.site.register(apartment)
admin.site.register(rental)

# Register your models here.
