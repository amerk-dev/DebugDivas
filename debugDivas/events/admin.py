from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'started_at', 'ended_at')
    list_filter = ('started_at', 'ended_at', 'max_age')
    search_fields = ('name', 'started_at')



admin.site.register(Event, EventAdmin)
