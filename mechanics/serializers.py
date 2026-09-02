from rest_framework import serializers
from .models import Mechanic, ServiceRequest


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'

class ServiceRequestSerializer(serializers.ModelSerializer):

    def validate_customer_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must be 10 digits."
            )

        return value

    def validate_vehicle_number(self, value):
        value = value.upper()

        if len(value) < 6:
            raise serializers.ValidationError(
                "Invalid vehicle number."
            )

        return value

    def validate_service(self, value):
        allowed_services = [
        "Oil Change",
        "Brake Repair",
        "Engine Repair",
        "Tire Change"
    ]

        if value not in allowed_services:
            raise serializers.ValidationError(
            "Invalid service."
        )

        return value

    class Meta:
        model = ServiceRequest
        fields = '__all__'