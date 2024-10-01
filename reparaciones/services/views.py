from rest_framework import viewsets, generics, authentication, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import PaymentMethod, Status, ServiceType, Service, ServiceHistory, Payments
from .serializers import PaymentMethodSerializer, StatusSerializer, ServiceTypeSerializer, ServiceSerializer, ServiceHistorySerializer, PaymentsSerializer

# Create your views here.

# Modelos pequeños

# Vistas de PaymentMethod (CRUD)
class ListPaymentMethodView(generics.ListAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

class CreatePaymentMethodView(generics.CreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]


class RetrievePaymentMethodView(generics.RetrieveAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class UpdatePaymentMethodView(generics.UpdateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]

class DestroyPaymentMethodView(generics.DestroyAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]


# Vistas de Status (CRUD)
class ListStatusView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    
class CreateStatusView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class RetrieveStatusView(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UpdateStatusView(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DestroyStatusView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
# Vistas de ServiceType (CRUD)
class ListServiceTypeView(generics.ListAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

class CreateServiceTypeView(generics.CreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class RetrieveServiceTypeView(generics.RetrieveAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UpdateServiceTypeView(generics.UpdateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DestroyServiceTypeView(generics.DestroyAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
# Modelos principales

# Vistas de Service (CRUD)
class ListServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

class CreateServiceView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class RetrieveServiceView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class UpdateServiceView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class DestroyServiceView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    

# Vistas de ServiceHistory (CRUD)
class ListServiceHistoryView(generics.ListAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

class CreateServiceHistoryView(generics.CreateAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class RetrieveServiceHistoryView(generics.RetrieveAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UpdateServiceHistoryView(generics.UpdateAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DestroyServiceHistoryView(generics.DestroyAPIView):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
# Vistas de Payments
class ListPaymentsView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

class CreatePaymentsView(generics.CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class RetrievePaymentsView(generics.RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UpdatePaymentsView(generics.UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DestroyPaymentsView(generics.DestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
