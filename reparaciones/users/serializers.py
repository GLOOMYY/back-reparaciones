from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from .models import User, Client, IdentificationType

# Serializadores Basicos
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create_user(self, validated_data):
        return get_user_model.objects.create_user(**validated_data)

    def update_user(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    def validate_password(self, value):
        return make_password(value)

    # Borrar borrado logico
    def delete_user(self, instance, validated_data):
        password = validated_data.pop(None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()


class AuthTokenSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"), username=email, password=password
        )

        if not user:
            raise serializers.ValidationError(
                "El usuario no se pudo autenticar", code="authorization"
            )

        attrs["user"] = user

        return attrs


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class IdentificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationType
        fields = "__all__"

# Serializadores contadores
class CountClientSerializer(serializers.Serializer):
    total = serializers.IntegerField()

# Serializadores combinados