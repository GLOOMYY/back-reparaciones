from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from models import User, Client, IdentificationType

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create_user(self):
        pass
    
    def update_user(self):
        pass
    
    def delete_user(self):
        pass
    
    def validate_password(self):
        pass
        
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def create_client(self):
        pass
    
    def update_client(self):
        pass
    
    def delete_client(self):
        pass
    

class IdentificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationType
        fields = "__all__"
        
    def create_identification_type(self):
        pass
    
    def update_identification_type(self):
        pass
    
    def delete_identification_type(self):
        pass

