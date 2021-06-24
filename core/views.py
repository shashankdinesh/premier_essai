from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
import base64
from io import BytesIO, StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from datetime import datetime
import logging
import random

from django.contrib.auth import authenticate

# Create your views here.
from django.core import management
from django_common.auth_backends import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import upload_contract
from econtract import errors
from core import serializers, utils
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout
from core.models import User as core_user, Contract
from django.core.files import File
APPLICATION_NAME = "core"

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'  # items per page


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserCreateSerializer
    permission_classes = (AllowAny,)
    http_method_names = ["post"]

    __doc__ = "Registration API for user"

    def create(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        data = request.data
        logging.info("registration api called with data {}".format(str(data)))
        if data.get("email"):
            data["email"] = data["email"].lower()
            if User.objects.filter(email=data["email"]):
                return Response(
                    {
                        "status": False,
                        "message": "Email already exists"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if data.get("username"):
            data["username"] = data["username"].lower()
            if User.objects.filter(username=data.get("username")):
                return Response(
                    {
                        "status": False,
                        "message": "username already exists"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        logging.info(user.__dict__)

        tokens = utils.get_tokens_for_user(user)

        return Response(
            {
                "status": True,
                "AccessToken": tokens["access"],
                "RefreshToken": tokens["refresh"],
            },
            status=status.HTTP_201_CREATED,
        )


class ObtainTokenLogin(APIView):
    def post(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        logging.info(f"login request for {request.data}")
        if "username" not in request.data:
            logging.info(f"username not supplied")
            return Response(
                {"status": False, "username": errors.FIELD_REQUIRED},
                status=status.HTTP_200_OK,
            )
        if "password" not in request.data:
            logging.info(f"password not supplied required")
            return Response(
                {"status": False, "password": errors.FIELD_REQUIRED},
                status=status.HTTP_200_OK,
            )

        logging.info(f"looking for user")
        user = User.objects.filter(username=request.data["username"]).first()
        if not user:
            logging.info(f"{user} not found")
            return Response(
                {"status": False, "user": errors.USER_NOT_EXIST},
                status=status.HTTP_200_OK,
            )
        if not user.is_active:
            logging.info(f"{user} account disabled")
            msg = errors.ACCOUNT_DISABLED_CONTACT_SUPPORT
            raise serializers.ValidationError(msg)
        credentials = {
            "username": request.data["username"],
            "password": request.data["password"],
        }

        user = authenticate(**credentials)
        if user:
            logging.info(f"{user} generating access tokens")
            tokens = utils.get_tokens_for_user(user)

            return Response(
                {
                    "message": "You have successfully Logged In",
                    "status": True,
                    "AccessToken": tokens["access"],
                    "RefreshToken": tokens["refresh"],
                },
                status=status.HTTP_200_OK,
            )
        else:
            logging.info(f"wrong credentials supplied")
            return Response(
                {
                    "message": "email or password does not match, please enter correct details",
                    "status": False,
                },
                status=status.HTTP_200_OK,
            )


class RefreshTokenApiView(APIView):
    """
    refresh token api to get new access token using refresh token from login api
    """

    def post(self, request, *args, **kwargs):
        if not request.data.get("refresh", None):
            return Response({"status": False, "message": "Refresh Token not found"})
        refresh_token = request.data["refresh"]
        try:
            tokens = utils.refresh_tokens_for_user(refresh_token)
        except:
            return Response(
                {
                    "status": False,
                    "message": "No user found related to given refresh token, or refresh token is expired",
                },
                status= status.HTTP_401_UNAUTHORIZED
            )

        return Response({"status": True, "AccessToken": tokens["access"],
                 "RefreshToken": tokens["refresh"]})



class UploadContract(generics.CreateAPIView):
    serializer_class = serializers.ContractSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        contract_qs = Contract.objects.filter(created_by=self.request.user.id)
        return contract_qs

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"status": True, "data": serializer.data},status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        request.data['created_by']=request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class GetRecievedContractListAPIView(generics.ListAPIView):

    serializer_class = serializers.ContractSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        recieved_contract_qs = User.objects.get(id=self.request.user.id).recieved_contract.all()
        return recieved_contract_qs

    def get(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()

        queryset = self.get_queryset()
        if queryset:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(
                {"status": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": True, "data": []}, status=status.HTTP_204_NO_CONTENT
            )


class GetReviewContractListAPIView(generics.ListAPIView):
    serializer_class = serializers.ContractSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        review_contract_qs = User.objects.get(id=self.request.user.id).contract_reviewer.all()
        return review_contract_qs

    def get(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()

        queryset = self.get_queryset()
        if queryset:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(
                {"status": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": True, "data": []}, status=status.HTTP_204_NO_CONTENT
            )

class UpdateContractDataAPIView(generics.UpdateAPIView):

    serializer_class = serializers.ContractSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            instance = Contract.objects.get(id=kwargs["pk"])
            serializer = self.get_serializer(instance)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"status": False, "message": "contract not found"}, status=status.HTTP_204_NO_CONTENT)


    def update(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        approving_user = request.data.get('user_approved',None)
        approving_reviewer = request.data.get('user_reviewed',None)
        updated_contract = request.data.get('upload',None)
        update_contract_date = request.data.get('contract_update_date',None)

        if updated_contract and not update_contract_date:
            request.data['contract_update_date'] = datetime.today().date().strftime("%Y-%m-%d")

        partial = kwargs.pop("partial", False)
        try:
            instance = Contract.objects.get(id=kwargs["pk"])
            if approving_user:
                valid_approvers = [inst.id for inst in instance.other_party_user.all()]
                for user in approving_user:
                    if not user in valid_approvers:
                        return Response(
                            {"status": False, "message": f"approving user {user} is not in other party user list {valid_approvers}"}, status=status.HTTP_400_BAD_REQUEST

                        )
            if approving_reviewer:
                valid_reviewers = [inst.id for inst in instance.reviewer_user.all()]
                for user in approving_reviewer:
                    if not user in valid_reviewers:
                        return Response(
                            {"status": False, "message": f"Reviewing user {user} is not in Review user list {valid_reviewers}"},
                            status=status.HTTP_400_BAD_REQUEST

                        )

        except Exception as ex:
            logging.exception(f"exception in fetcing instance {ex}")
            return Response(
                {"status": False, "data": []}, status=status.HTTP_204_NO_CONTENT
            )

        serializer = self.serializer_class(
            instance, data=request.data, partial=partial,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": True, "message": "Data Saved Successfully"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response({"status": False}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


class UploadFileS3(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()

        file = request.data.get("file", None)
        filename = file.name if file else None

        if file and filename:
            logging.info(f"file name is {filename}")
            path=upload_contract(file, filename)
            logging.info(f"file path is {path}")
            if path:
                return Response({"status": True,"filename":filename, "path":path, "message": "Contract Uploaded Successfully"},status=status.HTTP_201_CREATED)
            else:
                return Response({"status": False, "message": "Contract Upload Failed"},
                     status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": False, "message": "No contract Found to upload"},
                            status=status.HTTP_400_BAD_REQUEST)

