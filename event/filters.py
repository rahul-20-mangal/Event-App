import django_filters 
from django_filters import DateRangeFilter,DateFilter
from .models import Event, Timing

class TimingFilter(django_filters.FilterSet):

    event_year = django_filters.NumberFilter(field_name='event_date', lookup_expr='year', label='Event year')
    event_year__gt = django_filters.NumberFilter(field_name='event_date', lookup_expr='year__gt')
    event_year__lt = django_filters.NumberFilter(field_name='event_date', lookup_expr='year__lt')
    event_month = django_filters.NumberFilter(field_name='event_date', lookup_expr='month')
    event_day = django_filters.NumberFilter(field_name='event_date', lookup_expr='day')
    event_between_dates = django_filters.DateFromToRangeFilter(field_name='event_date', label='Events between dates')

    class Meta:
        model = Timing
        fields = ['event_date', 'event_time']

   

  