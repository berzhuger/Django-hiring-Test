from rest_framework import serializers
from rest_api.models import Location, Temperatures


class TemperaturesSerializer(serializers.ListSerializer):
    temperatures = serializers.DecimalField(max_digits=3, decimal_places=1)


class LocationSerializer(serializers.ModelSerializer):
    temperatures = TemperaturesSerializer(child=serializers.FloatField())

    class Meta:
        model = Location
        fields = ('id', 'date', 'lon', 'lat', 'city', 'state', 'temperatures')

    def create(self, validated_data):
        temperatures_data = validated_data.pop('temperatures')
        location = Location.objects.create(**validated_data)
        for temperature in temperatures_data:
            Temperatures.objects.create(location=location, temperatures=temperature)
        return location
