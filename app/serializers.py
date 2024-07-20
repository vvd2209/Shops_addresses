from rest_framework import serializers
from app.models import City, Shop, Street


class CitySerializer(serializers.ModelSerializer):
    """ Сериалализатор для модели City """
    class Meta:
        model = City
        fields = ("id", "name",)


class StreetSerializer(serializers.ModelSerializer):
    """ Сериалализатор для модели Street """
    class Meta:
        model = Street
        fields = ("id", "name", "city",)


class ShopWriteSerializer(serializers.ModelSerializer):
    """ Сериалализатор для модели Shop - запись данных """
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    street = serializers.PrimaryKeyRelatedField(queryset=Street.objects.all())

    class Meta:
        model = Shop
        fields = ("id", "name", "city", "street", "house", "opening_time", "closing_time",)


class ShopReadSerializer(serializers.ModelSerializer):
    """ Сериалализатор для модели Shop - чтение данных """
    city = serializers.CharField(source='street.city.name', read_only=True)
    street = serializers.CharField(source='street.name', read_only=True)

    class Meta:
        model = Shop
        fields = ("id", "name", "city", "street", "house", "opening_time", "closing_time",)
