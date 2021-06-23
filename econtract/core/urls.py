from django.urls import path

from core import views
from rest_framework.authtoken import views as authtoken_views

app_name = "core"

urlpatterns = [
    path(
        "api-token-auth/",
        authtoken_views.obtain_auth_token
    ),
    path(
        "register/",
        views.RegistrationAPIView.as_view(),
        name="register"
    ),
    path(
        "upload_contract/",
        views.UploadContract.as_view(),
        name="upload_contract"
    ),
    path(
        "recieved_contract/",
        views.GetRecievedContractListAPIView.as_view(),
        name="recieved-contract"
    ),
    path(
        "update/<int:pk>/",
        views.UpdateContractDataAPIView.as_view(),
        name="update-contract"
    ),
    path(
        "login/",
        views.ObtainTokenLogin.as_view(),
        name="login",
    ),
]