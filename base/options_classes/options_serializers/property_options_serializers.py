from rest_framework.serializers import Serializer
from rest_framework import serializers


class PropertyTypeSerializers(Serializer):
    property_type = serializers.CharField(max_length=500)


class SellerTypeSerializer(Serializer):
    seller_type = serializers.CharField(max_length=300)


class BrokerFeeSerializer(Serializer):
    broker_fee = serializers.Charfield(max_length=500)


class FurnishingSerializer(Serializer):
    furnishing = serializers.Charfield(max_length=300)


class Number0fOwnersSerializers(Serializer):
    number_of_owners = serializers.CharField(max_length=200)


class NumberOfOwnersSerializers(Serializer):
    number_of_owners = serializers.Charfield(max_length=300)


class FencedSerializers(Serializer):
    fenced = serializers.CharField(max_length=200)
