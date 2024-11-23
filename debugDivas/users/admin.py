from django.contrib import admin
from .models import CustomUser, SportType, Location


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        CustomUser.email.field.name,
        CustomUser.tg_username.field.name, 
        CustomUser.sport_type.field.name, 
        CustomUser.is_active.field.name, 
        CustomUser.date_joined.field.name
    )


class SportTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SportType, SportTypeAdmin)
admin.site.register(Location, LocationAdmin)