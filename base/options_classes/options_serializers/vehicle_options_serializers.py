from rest_framework.serializers import Serializer
from rest_framework import serializers


class FuelTypeSerializers(Serializer):
    fuel_type = serializers.CharField(max_length=500)


class BodyTypeSerializer(Serializer):
    body_type = serializers.CharField(max_length=300)


class transmissionSerializer(Serializer):
    transmission = serializers.Charfield(max_length=500)


class VehicleConditionSerializer(Serializer):
    vehicle_condition = serializers.Charfield(max_length=300)


class VehicleColourSerializers(Serializer):
    vehicle_colour = serializers.CharField(max_length=200)


class NumberOfOwnersSerializers(Serializer):
    number_of_owners = serializers.Charfield(max_length=300)


class VehicleMakeSerializers(Serializer):
    vehicle_make = serializers.CharField(max_length=200)


class CarModelSerializers(Serializer):
    car_model = serializers.CharField(max_length=300) 