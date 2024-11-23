from django_filters import rest_framework as filters
from .models import Event

class EventFilter(filters.FilterSet):
    sport_type = filters.NumberFilter(field_name='sport_type__id')
    location = filters.NumberFilter(field_name='location__id')
    seats = filters.RangeFilter()
    gender = filters.BooleanFilter()
    age = filters.RangeFilter(field_name='min_age', lookup_expr='lte')
    started_at = filters.DateTimeFromToRangeFilter()
    ended_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Event
        fields = ['sport_type', 'location', 'seats', 'gender', 'age', 'started_at', 'ended_at']