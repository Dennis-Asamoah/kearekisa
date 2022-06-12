from rest_framework.serializers import Serializer
from rest_framework import serializers


class BrandSerializers(Serializer):
    brand = serializers.CharField(max_length=500)


class ModelSerializer(Serializer):
    model = serializers.CharField(max_length=300)


class ConditionSerializer(Serializer):
    condition = serializers.Charfield(max_length=500)
