from django.db import models
# importamos la clase abstracta de usuarios:
from django.contrib.auth.models import (
    AbstractUser,
    PermissionsMixin,
    BaseUserManager,
)

# Clases pequeñas
class IdentificationType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tipo de Identificación"
        verbose_name_plural = "Tipos de Identificación"
    
    def __str__(self):
        return self.name

# Clases principales
class UserManager(BaseUserManager):
    def createUser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El email debe ser obligatorio')
        
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        
        user.is_active = True

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.createUser(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        
        return user



class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Correo Electrónico', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    type_id = models.ForeignKey(to=IdentificationType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Tipo de Identificación')
    identification = models.CharField(verbose_name='Número de Identificación', max_length=50)
    name = models.CharField(verbose_name='Nombre', max_length=50, null=True, blank=True)
    username = models.CharField(verbose_name='Usuario', max_length=50)
    photo = models.ImageField(verbose_name='Foto de Perfil', upload_to='img/usuarios/', null=True, blank=True)
    
    country = models.CharField(verbose_name='Pais de Residencia', max_length=255)
    city = models.CharField(verbose_name='Ciudad de Residencia', max_length=255)
    address = models.TextField(verbose_name='Direccion de Residencia', max_length=255, null=True, blank=True)
    phone = models.CharField(verbose_name='Teléfono', max_length=20, null=True, blank=True)
    
    birthday = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    class Meta:
        verbose_name ="User"
        verbose_name_plural ="Users"

    def __str__(self):
        return f'{self.username} - {self.name}'

class Client(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, verbose_name='Usuario', null=True, blank=True)
    name = models.CharField(verbose_name='Nombre', max_length=50, null=True, blank=True)
    email = models.EmailField(verbose_name='Correo Electrónico', null=True, blank=True)
    address = models.TextField(verbose_name='Direccion de Residencia', max_length=255, null=True, blank=True)
    phone = models.CharField(verbose_name='Teléfono', max_length=20, null=True, blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"
        
    def __str__(self):
        return f'{self.name} - {self.phone} - {self.email}'
    
