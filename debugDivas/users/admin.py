from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, SportType, Location


class UserAdmin(BaseUserAdmin):
    # Поля, отображаемые в списке пользователей
    list_display = ('tg_username', 'full_name', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'sport', 'location')
    search_fields = ('tg_username', 'full_name', 'email')
    ordering = ('tg_username',)

    # Поля, отображаемые в форме пользователя
    fieldsets = (
        (None, {'fields': ('tg_username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'email', 'sport', 'location')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Tokens', {'fields': ('access_token', 'refresh_token')}),
        ('Important dates', {'fields': ('last_login',)})
    )

    # Поля, которые отображаются при создании нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('tg_username', 'full_name', 'password1', 'password2', 'sport', 'location', 'is_superuser')}
        ),
    )


class SportTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)



admin.site.register(CustomUser, UserAdmin)
admin.site.register(SportType, SportTypeAdmin)
admin.site.register(Location, LocationAdmin)