from decimal import Decimal
from django.db.models import Q
import django_filters
from .models import Employee


class ProductFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Employee
        fields = ['query']

    def universal_search(self, queryset, name, value):
        return Employee.objects.filter(
            Q(position__bio__first_name=value) | Q(position__bio__last_name=value)
            | Q(position__position_name=value)
        )
