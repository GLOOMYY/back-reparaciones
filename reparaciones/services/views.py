from django.shortcuts import render
from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from django_filters.rest_framework import DjangoFilterBackend
from .models import PaymentMethod, Status, ServiceType, Service, ServiceHistory, Payments
from .serializers import PaymentMethodSerializer, StatusSerializer, ServiceTypeSerializer, ServiceSerializer, ServiceHistorySerializer, PaymentsSerializer

# Create your views here.

# Modelos pequeños

# Vistas de PaymentMethod (CRUD)
class ListPaymentMethodView(generics.ListAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    filter_backends = [DjangoFilterBackend]

class CreatePaymentMethodView(generics.CreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class RetrievePaymentMethodView(generics.RetrieveAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    

class UpdatePaymentMethodView(generics.UpdateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class DestroyPaymentMethodView(generics.DestroyAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


# Vistas de Status (CRUD)
class ListStatusView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = [DjangoFilterBackend]
    
class CreateStatusView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class RetrieveStatusView(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
class UpdateStatusView(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
class DestroyStatusView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
    
# Vistas de ServiceType (CRUD)
class ListServiceTypeView(generics.ListAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    filter_backends = [DjangoFilterBackend]

class CreateServiceTypeView(generics.CreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    
class RetrieveServiceTypeView(generics.RetrieveAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    
class UpdateServiceTypeView(generics.UpdateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    
class DestroyServiceTypeView(generics.DestroyAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    
    
# Modelos principales

# Vistas de Service (CRUD)
class ListServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]

class CreateServiceView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class RetrieveServiceView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class UpdateServiceView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class DestroyServiceView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    

# Vistas de ServiceHistory (CRUD)
class ListServiceHistoryView(generics.ListAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    filter_backends = [DjangoFilterBackend]

class CreateServiceHistoryView(generics.CreateAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    
class RetrieveServiceHistoryView(generics.RetrieveAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    
class UpdateServiceHistoryView(generics.UpdateAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    
class DestroyServiceHistoryView(generics.DestroyAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    
    
# Vistas de Payments
class ListPaymentsView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend]

class CreatePaymentsView(generics.CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    
class RetrievePaymentsView(generics.RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    
class UpdatePaymentsView(generics.UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    
class DestroyPaymentsView(generics.DestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    
