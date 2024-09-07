from django.shortcuts import render
from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User, Client, IdentificationType 
from .serializers import UserSerializer, ClientSerializer, IdentificationTypeSerializer

# Create your views here.

# Vistas de User (CRUD)
class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DestroyUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Vistas de Client (CRUD)

class ListClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CreateClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class RetrieveClientView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class UpdateClientView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DestroyClientView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Vistas de IdentificacionType (CRUD)
class ListIdentificationTypeView(generics.ListAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer

class CreateIdentificationTypeView(generics.CreateAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer

class RetrieveIdentificationTypeView(generics.RetrieveAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer

class UpdateIdentificationTypeView(generics.UpdateAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer

class DestroyIdentificationTypeView(generics.DestroyAPIView):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer