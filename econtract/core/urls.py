from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
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