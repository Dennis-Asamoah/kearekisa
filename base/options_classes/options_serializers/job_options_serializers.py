from rest_framework.serializers import Serializer
from rest_framework import serializers


class ContractTypeSerializers(Serializer):
    contract_type = serializers.CharField(max_length=500)


class WorkingHoursSerializer(Serializer):
    working_hours = serializers.CharField(max_length=300)
