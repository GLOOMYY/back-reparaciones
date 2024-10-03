from django.urls import path, include
from rest_framework import routers

# Importe PaymentMethod
from .views import ListPaymentMethodView, CreatePaymentMethodView, RetrievePaymentMethodView, UpdatePaymentMethodView, DestroyPaymentMethodView

# Importe Status
from .views import ListStatusView, CreateStatusView, RetrieveStatusView, UpdateStatusView, DestroyStatusView

# Importe ServiceType
from .views import ListServiceTypeView, CreateServiceTypeView, RetrieveServiceTypeView, UpdateServiceTypeView, DestroyServiceTypeView

# Importe Service
from .views import ListServiceView, CreateServiceView, RetrieveServiceView, UpdateServiceView, DestroyServiceView

# Importe ServiceHistory
from .views import ListServiceHistoryView, CreateServiceHistoryView, RetrieveServiceHistoryView, UpdateServiceHistoryView, DestroyServiceHistoryView

# Importe Payments
from .views import ListPaymentsView, CreatePaymentsView, RetrievePaymentsView, UpdatePaymentsView, DestroyPaymentsView

# Import Resumes
from .views import ResumeServiceListView


urls_payment_method = [
    path("payment-method/list", ListPaymentMethodView.as_view(), name = "payment-method-lista"),
    path("payment-method/create", CreatePaymentMethodView.as_view(), name = "payment-method-crear"),
    path("payment-method/retrieve/<int:pk>", RetrievePaymentMethodView.as_view(), name = "payment-method-detalle"),
    path("payment-method/update/<int:pk>", UpdatePaymentMethodView.as_view(), name = "payment-method-actualizar"),
    path("payment-method/destroy/<int:pk>", DestroyPaymentMethodView.as_view(), name = "payment-method-eliminar"),
]

urls_status = [
    path("status/list", ListStatusView.as_view(), name = "status-lista"),
    path("status/create", CreateStatusView.as_view(), name = "status-crear"),
    path("status/retrieve/<int:pk>", RetrieveStatusView.as_view(), name = "status-detalle"),
    path("status/update/<int:pk>", UpdateStatusView.as_view(), name = "status-actualizar"),
    path("status/destroy/<int:pk>", DestroyStatusView.as_view(), name = "status-eliminar"),
]

urls_service = [
    path("service/list", ListServiceView.as_view(), name = "service-lista"),
    path("service/create", CreateServiceView.as_view(), name = "service-crear"),
    path("service/retrieve/<int:pk>", RetrieveServiceView.as_view(), name = "service-detalle"),
    path("service/update/<int:pk>", UpdateServiceView.as_view(), name = "service-actualizar"),
    path("service/destroy/<int:pk>", DestroyServiceView.as_view(), name = "service-eliminar"),
]

urls_service_type = [
    path("service-type/list", ListServiceTypeView.as_view(), name = "service-type-lista"),
    path("service-type/create", CreateServiceTypeView.as_view(), name = "service-type-crear"),
    path("service-type/retrieve/<int:pk>", RetrieveServiceTypeView.as_view(), name = "service-type-detalle"),
    path("service-type/update/<int:pk>", UpdateServiceTypeView.as_view(), name = "service-type-actualizar"),
    path("service-type/destroy/<int:pk>", DestroyServiceTypeView.as_view(), name = "service-type-eliminar"),
]

urls_service_history = [
    path("service-history/list", ListServiceHistoryView.as_view(), name = "service-history-lista"),
    path("service-history/create", CreateServiceHistoryView.as_view(), name = "service-history-crear"),
    path("service-history/retrieve/<int:pk>", RetrieveServiceHistoryView.as_view(), name = "service-history-detalle"),
    path("service-history/update/<int:pk>", UpdateServiceHistoryView.as_view(), name = "service-history-actualizar"),
    path("service-history/destroy/<int:pk>", DestroyServiceHistoryView.as_view(), name = "service-history-eliminar"),
]

urls_payments = [
    path("payments/list", ListPaymentsView.as_view(), name = "payments-lista"),
    path("payments/create", CreatePaymentsView.as_view(), name = "payments-crear"),
    path("payments/retrieve/<int:pk>", RetrievePaymentsView.as_view(), name = "payments-detalle"),
    path("payments/update/<int:pk>", UpdatePaymentsView.as_view(), name = "payments-actualizar"),
    path("payments/destroy/<int:pk>", DestroyPaymentsView.as_view(), name = "payments-eliminar"),
]

urls_resume = [
    path("resume/service", ResumeServiceListView.as_view(), name = "resume-service")
]

urlpatterns = urls_payment_method + urls_status + urls_service + urls_service_type + urls_service_history + urls_payments + urls_resume
