from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_at', 'end_at', 'active', 'following_user', 'followed_user')
    list_filter = ('active', 'start_at', 'end_at', 'min_age', 'max_age')
    search_fields = ('name', 'following_user__tg_username', 'followed_user__tg_username')