from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from .models import Service, ServiceHistory, Payments, PaymentMethod, Status, ServiceType

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
        
    def create_service(self):
        pass
    
    def update_service(self):
        pass
    
    def delete_service(self):
        pass

class ServiceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHistory
        fields = "__all__"

    def create_service_history(self):
        pass
    
    def update_service_history(self):
        pass
    
    def delete_service_history(self):
        pass

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"

    def create_payment(self):
        pass
    
    def update_payment(self):
        pass
    
    def delete_payment(self):
        pass

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"

    def create_payment_method(self, validated_data):
        method = PaymentMethod.objects.create(validated_data)
        return method
    
    def update_payment_method(self):
        pass
    
    def delete_payment_method(self):
        pass

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"

    def create_status(self):
        pass
    
    def update_status(self):
        pass
    
    def delete_status(self):
        pass

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"

    def create_service_type(self):
        pass
    
    def update_service_type(self):
        pass
    
    def delete_service_type(self):
        pass