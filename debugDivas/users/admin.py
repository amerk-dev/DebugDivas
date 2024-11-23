from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        CustomUser.email.field.name,
        CustomUser.tg_username.field.name, 
        CustomUser.sport_type.field.name, 
        CustomUser.is_active.field.name, 
        CustomUser.date_joined.field.name,
    )
    can_delete = False



admin.site.register(CustomUser, CustomUserAdmin)