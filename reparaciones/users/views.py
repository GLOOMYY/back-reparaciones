from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Client, IdentificationType
from .serializers import (
    UserSerializer,
    ClientSerializer,
    IdentificationTypeSerializer,
    AuthTokenSerializers,
)

# Create your views here.


# Vistas de User (CRUD)
class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class DestroyUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Vistas de Client (CRUD)


class ListClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]


class CreateClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class RetrieveClientView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UpdateClientView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class DestroyClientView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Vistas de IdentificacionType (CRUD)
class ListIdentificationTypeView(generics.ListAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]


class CreateIdentificationTypeView(generics.CreateAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class RetrieveIdentificationTypeView(generics.RetrieveAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UpdateIdentificationTypeView(generics.UpdateAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class DestroyIdentificationTypeView(generics.DestroyAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
