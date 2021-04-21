import django_filters
from .models import *
from django_filters import DateFilter,CharFilter,DateFromToRangeFilter

class CustomerFilter(django_filters.FilterSet):
    created_date = DateFilter(field_name='created_date' ,lookup_expr='icontains')
    addr = CharFilter(field_name='addr', lookup_expr='icontains')
    class Meta:
        model = Customer
        fields = '__all__'

class VisitsFilter(django_filters.FilterSet):
    created_date = DateFilter(field_name='created_date', lookup_expr='icontains')
    narration = CharFilter(field_name='narration', lookup_expr='icontains')
    class Meta:
        model = Visits
        fields = '__all__'
