from django.db import models
from users.models import User, Client

# Modelos pequeños
class PaymentMethod(models.Model):
    name = models.CharField(verbose_name="Metodo de pago" ,max_length=50, unique=True)
    
    class Meta:
        verbose_name = "Metodo de pago"
        verbose_name_plural = "Metodos de pago"
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    name = models.CharField(verbose_name="Estado" ,max_length=50, unique=True)
    
    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
    
    def __str__(self):
        return self.name
    
class ServiceType(models.Model):
    name = models.CharField(verbose_name="Tipo de servicio" ,max_length=200)
    
    class Meta:
        verbose_name = "Tipo de servicio"
        verbose_name_plural = "Tipos de servicios"
    
    def __str__(self):
        return self.name
    

# Modelos principales
class Service(models.Model):
    user = models.ForeignKey(to = User, verbose_name="Usuario", on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(to = Client, verbose_name="Cliente", on_delete=models.SET_NULL, null=True, blank=True)
    service_type = models.ForeignKey(to = ServiceType ,verbose_name="Tipo de servicio", on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(verbose_name="Descripcion del servicio", null=True, blank=True)
    status = models.ForeignKey(to = Status,verbose_name="Estado del servicio", on_delete=models.SET_NULL, null=True, blank=True)
    cost = models.DecimalField(verbose_name="Costo del servicio", max_digits=10, decimal_places=2 ,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    
    def __str__(self):
        return f"{self.client}: {self.service_type}"
    
class ServiceHistory(models.Model):
    service = models.ForeignKey(to = Service, verbose_name="Servicio", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(to = Status, verbose_name="Estado", on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(verbose_name="Nota", null=True, blank=True)
    received_at = models.DateField(verbose_name="Fecha de Recibido", null=True, blank=True)
    completed_at = models.DateField(verbose_name="Fecha de Entrega", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"
    
    def __str__(self):
        return f"{self.service}: {self.status}"
    
class Payments(models.Model):
    service = models.ForeignKey(to = Service, verbose_name="Servicio", on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(verbose_name="Costo", max_digits=10, decimal_places=2, null=True, blank=True)
    payment_date = models.DateField(verbose_name="Fecha de Pago", null=True, blank=True)
    payment_method = models.ForeignKey(to = PaymentMethod, verbose_name="Metodo de pago", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
    
    def __str__(self):
        return f"{self.service}: {self.payment_method} - {self.amount}"
