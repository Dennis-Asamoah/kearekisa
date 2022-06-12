from rest_framework import serializers
from rest_framework.serializers import Serializer


class PetAgeSerializers(Serializer):
    pet_age = serializers.CharField(max_length=200)


class DogBreedSerializers(Serializer):
    dog_breed = serializers.CharField(max_length=200)


class CatBreedSerializers(Serializer):
    cat_breed = serializers.CharField(max_length=200)