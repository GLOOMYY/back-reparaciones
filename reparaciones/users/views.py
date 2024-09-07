from django.shortcuts import render
from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User, Client, IdentificationType 
from .serializers import UserSerializer, ClientSerializer, IdentificationTypeSerializer

# Create your views here.

# Vistas de User (CRUD)
class ListUserView(generics.ListAPIView):
    queryset = User
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User
    serializer_class = UserSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = User
    serializer_class = UserSerializer

class UpdateUserView(generics.UpdateAPIView):
    queryset = User
    serializer_class = UserSerializer

class DestroyUserView(generics.DestroyAPIView):
    queryset = User
    serializer_class = UserSerializer

# Vistas de Client (CRUD)

class ListClientView(generics.ListAPIView):
    queryset = Client
    serializer_class = ClientSerializer

class CreateClientView(generics.CreateAPIView):
    queryset = Client
    serializer_class = ClientSerializer

class RetrieveClientView(generics.RetrieveAPIView):
    queryset = Client
    serializer_class = ClientSerializer

class UpdateClientView(generics.UpdateAPIView):
    queryset = Client
    serializer_class = ClientSerializer

class DestroyClientView(generics.DestroyAPIView):
    queryset = Client
    serializer_class = ClientSerializer

# Vistas de IdentificacionType (CRUD)
class ListIdentificationTypeView(generics.ListAPIView):
    queryset = IdentificationType
    serializer_class = IdentificationTypeSerializer

class CreateIdentificationTypeView(generics.CreateAPIView):
    queryset = IdentificationType
    serializer_class = IdentificationTypeSerializer

class RetrieveIdentificationTypeView(generics.RetrieveAPIView):
    queryset = IdentificationType
    serializer_class = IdentificationTypeSerializer

class UpdateIdentificationTypeView(generics.UpdateAPIView):
    queryset = IdentificationType
    serializer_class = IdentificationTypeSerializer

class DestroyIdentificationTypeView(generics.DestroyAPIView):
    queryset = IdentificationType
    serializer_class = IdentificationTypeSerializer