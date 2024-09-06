from django.shortcuts import render
from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User, Client, IdentificationType 
from .serializers import UserSerializer, ClientSerializer, IdentificationTypeSerializer

# Create your views here.

# Vistas de User (CRUD)
class CreateUserView():
    pass

class ReadUserView():
    pass

class UpdateUserView():
    pass

class DeleteUserView():
    pass

# Vistas de Client (CRUD)

class CreateClienteView():
    pass

class ReadClienteView():
    pass

class UpdateClienteView():
    pass

class DeleteClienteView():
    pass

# Vistas de IdentificacionType (CRUD)

class CreateIdentificationTypeView():
    pass

class ReadIdentificationTypeView():
    pass

class UpdateIdentificationTypeView():
    pass

class DeleteIdentificationTypeView():
    pass