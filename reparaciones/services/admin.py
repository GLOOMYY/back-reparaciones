from django.contrib import admin
from .models import (
    PaymentMethod,
    Status,
    ServiceType,
    Service,
    ServiceHistory,
    Payments,
)

# Register your models here.

admin.site.register(PaymentMethod)
admin.site.register(Status)
admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(ServiceHistory)
admin.site.register(Payments)