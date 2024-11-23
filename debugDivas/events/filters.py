from django_filters import rest_framework as filters
from .models import Event

class EventFilter(filters.FilterSet):
    ekp_id = filters.CharFilter(field_name='ekp_id')
    sport_type = filters.CharFilter(field_name='sport_type')
    location = filters.CharFilter(field_name='location')
    seats = filters.RangeFilter()
    gender = filters.BooleanFilter()
    age = filters.RangeFilter(field_name='min_age', lookup_expr='lte')
    started_at = filters.DateTimeFromToRangeFilter()
    ended_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Event
        fields = ['sport_type', 'location', 'seats', 'gender', 'age', 'started_at', 'ended_at']