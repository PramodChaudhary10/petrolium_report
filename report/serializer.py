from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.Serializer):
    year = serializers.CharField(max_length=100)
    petrolium_product = serializers.CharField(max_length=100)
    sales = serializers.IntegerField()
    country = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Report.objects.create(**validate_data)
