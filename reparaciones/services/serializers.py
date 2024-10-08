from rest_framework import serializers
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from django.contrib.auth.hashers import make_password
from .models import (
    Service,
    ServiceHistory,
    Payments,
    PaymentMethod,
    Status,
    ServiceType,
)
from users.serializers import ClientSerializer

# Serializadores basicos
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ServiceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHistory
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"


# Combinados

class ServiceResumeSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()  # Incluir datos completos del cliente
    service_type = ServiceTypeSerializer()  # Incluir datos completos del tipo de servicio
    status = StatusSerializer()  # Incluir datos completos del estado

    class Meta:
        model = Service
        fields = "__all__"

    # Método para personalizar los datos de cliente
    def get_client(self, obj):
        return {
            'id': obj.client.id,
            'name': obj.client.name,
            'email': obj.client.email
        }