from django.shortcuts import render
from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .models import PaymentMethod, Status, ServiceType, Service, ServiceHistory, Payments
from .serializers import PaymentMethodSerializer, StatusSerializer, ServiceTypeSerializer, ServiceSerializer, ServiceHistorySerializer, PaymentsSerializer

# Create your views here.

# Modelos pequeños

# Vistas de PaymentMethod (CRUD)
class CreatePaymentMethodView():
    pass

class ReadPaymentMethodView():
    pass

class UpdatePaymentMethodView():
    pass

class DeletePaymentMethodView():
    pass

# Vistas de Status (CRUD)
class CreateStatusView():
    pass

class ReadStatusView():
    pass

class UpdateStatusView():
    pass

class DeleteStatusView():
    pass

# Vistas de ServiceType (CRUD)
class CreateServiceTypeView():
    pass

class ReadServiceTypeView():
    pass

class UpdateServiceTypeView():
    pass

class DeleteServiceTypeView():
    pass

# Modelos principales

# Vistas de Service (CRUD)
class CreateServiceView():
    pass

class ReadServiceView():
    pass

class UpdateServiceView():
    pass

class DeleteServiceView():
    pass

# Vistas de ServiceHistory (CRUD)
class CreateServiceHistoryView():
    pass

class ReadServiceHistoryView():
    pass

class UpdateServiceHistoryView():
    pass

class DeleteServiceHistoryView():
    pass

# Vistas de Payments
class CreatePaymentsView():
    pass

class ReadPaymentsView():
    pass

class UpdatePaymentsView():
    pass

class DeletePaymentsView():
    pass


# Prueba
class RetrieveUpdateDestroyPaymentMethodView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer