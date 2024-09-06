from django.urls import path, include
from rest_framework import routers
from .views import RetrieveUpdateDestroyPaymentMethodView


urlpatterns = [
    path("<int:pk>", RetrieveUpdateDestroyPaymentMethodView.as_view())
]
