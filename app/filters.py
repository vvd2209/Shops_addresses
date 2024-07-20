from datetime import datetime

from django_filters.rest_framework import FilterSet, filters

from app.models import Shop


class ShopFilter(FilterSet):
    """ Фильтр для модели Shop по городу, улице и статусу
    param: Статус: закрыт - 0, открыт - 1 """
    street = filters.CharFilter(field_name='street__name', lookup_expr='icontains')
    city = filters.CharFilter(field_name='city__name', lookup_expr='icontains')
    open = filters.NumberFilter(method='filter_open')

    class Meta:
        model = Shop
        fields = ['street', 'city', 'open']

    def filter_open(self, queryset, name, value):
        """ Фильтр по статусу """
        current_time = datetime.now().time()

        if value == 1:
            return queryset.filter(opening_time__lte=current_time, closing_time__gte=current_time)
        elif value == 0:
            closed_morning = queryset.filter(opening_time__gte=current_time)
            closed_evening = queryset.filter(closing_time__lte=current_time)
            return closed_morning | closed_evening
        return queryset
