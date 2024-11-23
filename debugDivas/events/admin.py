from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = (
        Event.name.field.name,
        Event.started_at.field.name,
        Event.ended_at.field.name
    )
    list_filter = (
        Event.started_at.field.name,
        Event.ended_at.field.name,
        Event.max_age.field.name
    )
    search_fields = (
        Event.name.field.name,
        Event.started_at.field.name,
    )



admin.site.register(Event, EventAdmin)
