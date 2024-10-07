from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Importe User
from .views import ListUserView, CreateUserView, RetrieveUserView, UpdateUserView, DestroyUserView

# Importe Client
from .views import ListClientView, CreateClientView, RetrieveClientView, UpdateClientView, DestroyClientView, CountClientView

# Importe IdentificationType
from .views import ListIdentificationTypeView, CreateIdentificationTypeView, RetrieveIdentificationTypeView, UpdateIdentificationTypeView, DestroyIdentificationTypeView

url_user = [
    # path("login", CreateTokenView.as_view(), name="login"),
    path("user/list", ListUserView.as_view(), name = "user-lista"),
    path("user/create", CreateUserView.as_view(), name = "user-crear"),
    path("user/retrieve/<int:pk>", RetrieveUserView.as_view(), name = "user-detalle"),
    path("user/update/<int:pk>", UpdateUserView.as_view(), name = "user-actualizar"),
    path("user/destroy/<int:pk>", DestroyUserView.as_view(), name = "user-eliminar"),
]

url_client = [
    path("client/list", ListClientView.as_view(), name = "client-lista"),
    path("client/create", CreateClientView.as_view(), name = "client-crear"),
    path("client/retrieve/<int:pk>", RetrieveClientView.as_view(), name = "client-detalle"),
    path("client/update/<int:pk>", UpdateClientView.as_view(), name = "client-actualizar"),
    path("client/destroy/<int:pk>", DestroyClientView.as_view(), name = "client-eliminar"),
    path("client/count", CountClientView.as_view(), name="client-count"),
] 

url_identification_type = [
    path("identification-type/list", ListIdentificationTypeView.as_view(), name = "identification-type-lista"),
    path("identification-type/create", CreateIdentificationTypeView.as_view(), name = "identification-type-crear"),
    path("identification-type/retrieve/<int:pk>", RetrieveIdentificationTypeView.as_view(), name = "identification-type-detalle"),
    path("identification-type/update/<int:pk>", UpdateIdentificationTypeView.as_view(), name = "identification-type-actualizar"),
    path("identification-type/destroy/<int:pk>", DestroyIdentificationTypeView.as_view(), name = "identification-type-eliminar"),
]

#Test JWT
url_token = [
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = url_user + url_client + url_identification_type + url_token