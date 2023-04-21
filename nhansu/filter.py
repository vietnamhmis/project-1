import django_filters
from django_filters import CharFilter
from .models import To_nhom


class To_Filter(django_filters.FilterSet):
    ten_to = CharFilter(field_name='ten_to', lookup_expr='icontains')
    class Meta:
        model = To_nhom
        fields = ['ten_to', 'bo_phan']

