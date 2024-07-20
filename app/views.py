from django.shortcuts import get_list_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from app.models import City, Shop, Street

from app.filters import ShopFilter
from app.serializers import (CitySerializer, ShopReadSerializer, ShopWriteSerializer, StreetSerializer, )


class CityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ Контроллер, реализующий операции с моделью City """
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(detail=True, methods=['get'])
    def street(self, request, pk):
        """ Получение улиц, принадлежащих определенному городу по id """
        streets = get_list_or_404(Street, city__id=pk)
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)

    def handle_exception(self, exc):
        return Response({'data': 'Bad request'}, status=400)


class ShopViewSet(viewsets.ModelViewSet):
    """ Контроллер, реализующий операции с моделью Shop """
    queryset = Shop.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShopReadSerializer
        return ShopWriteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'id': serializer.data['id']},
                        status=status.HTTP_201_CREATED)

    def handle_exception(self, exc):
        return Response({'data': 'Bad request'}, status=400)
