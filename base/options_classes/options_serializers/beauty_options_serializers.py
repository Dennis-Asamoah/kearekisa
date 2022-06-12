from rest_framework.serializers import Serializer
from rest_framework import serializers


class HairSerializers(Serializer):
    hair = serializers.CharField(max_length=500)


class ColourSerializer(Serializer):
    colour = serializers.CharField(max_length=300)


class GenderSerializer(Serializer):
    gender = serializers.Charfield(max_length=500)


class AgeGroupSerializer(Serializer):
    age_group = serializers.Charfield(max_length=300)


class SkinTypeSerializers(Serializer):
    skin_type = serializers.CharField(max_length=200)


class ShoeSizeSerializers(Serializer):
    shoe_size = serializers.Charfield(max_length=300)


class DressSizeSerializers(Serializer):
    dress_size = serializers.CharField(max_length=200)


class GeneralSizeSerializers(Serializer):
    general_size = serializers.CharField(max_length=200)