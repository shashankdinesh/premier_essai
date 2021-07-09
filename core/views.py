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
import copy
from django.contrib.auth import authenticate

# Create your views here.
from django.core import management
from django_common.auth_backends import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import upload_contract, listbucketfile, delete_contract_data, delete_file, check_user_validity
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
                    status=status.HTTP_200_OK,
                )

        if data.get("username"):
            data["username"] = data["username"]
            if User.objects.filter(username=data.get("username")):
                return Response(
                    {
                        "status": False,
                        "message": "username already exists"
                    },
                    status=status.HTTP_200_OK,
                )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        logging.info(user.__dict__)
        update_status = serializer.update_contracts_details(serializer.instance)
        if update_status:
            logging.info("Contract details for registered user updated successfully")
        else:
            logging.info("Contract details updation for registered user failed")

        tokens = utils.get_tokens_for_user(user)

        return Response(
            {
                "message": "You have successfully Registered",
                "status": True,
                "AccessToken": tokens["access"],
                "RefreshToken": tokens["refresh"],
            },
            status=status.HTTP_201_CREATED,
        )


class ObtainTokenLogin(APIView):
    def post(self, request, *args, **kwargs):
        logging.info(f"login request for {request.data}")
        if "username" not in request.data:
            logging.info(f"username not supplied")
            return Response(
                {"status": False, "message": errors.FIELD_REQUIRED},
                status=status.HTTP_200_OK,
            )
        if "password" not in request.data:
            logging.info(f"password not supplied required")
            return Response(
                {"status": False, "message": errors.FIELD_REQUIRED},
                status=status.HTTP_200_OK,
            )

        logging.info(f"looking for user")
        user = User.objects.filter(username=request.data["username"]).first()
        if not user:
            logging.info(f"{user} not found")
            return Response(
                {"status": False, "message": errors.USER_NOT_EXIST},
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

    def get(self, request, *args, **kwargs):
        contract_status = self.request.GET.get('status',None)
        if not contract_status:
            return Response({"status": False, "message": "status not provided"}, status=status.HTTP_400_BAD_REQUEST)
        queryset = Contract.objects.filter(created_by=self.request.user.id, status=contract_status)
        if queryset:
            try:
                page = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response(serializer.data)

                serializer = self.get_serializer(queryset, many=True)
                return Response({"status": True, "data": serializer.data},status=status.HTTP_200_OK)
            except Exception as e:
                logging.info(e)
                return Response({"status": False, "message": e}, status=status.HTTP_400_BAD_REQUEST)
        else:
            logging.info("data not found")
            return Response({"status": False, "message": "Data Not Found"}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        other_party_ids,reviewer_ids=[],[]
        request.data['created_by']=request.user.id
        non_registered_other_users = copy.copy(request.data['non_registered_other_party_user'])
        non_registered_reviewer =  copy.copy(request.data['non_registered_reviewer_user'])
        for email in non_registered_other_users:
            if User.objects.filter(email=email):
                other_party_ids.append(User.objects.filter(email=email)[0].id)
                request.data['non_registered_other_party_user'].remove(email)

        request.data['other_party_user'] = other_party_ids

        for email in non_registered_reviewer:
            if User.objects.filter(email=email):
                reviewer_ids.append(User.objects.filter(email=email)[0].id)
                request.data['non_registered_reviewer_user'].remove(email)

        request.data['reviewer_user'] = reviewer_ids

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        mail_sent,msg = serializer.mail_contract_agreement_link(serializer.instance)
        if mail_sent:
            logging.info(msg)
        else:
            logging.info(msg)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GetContractListAPIView(generics.ListAPIView):
    serializer_class = serializers.ContractSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        queryset=None
        contract_status = self.request.data.get('status', None)
        if not contract_status:
            return Response(
                {"status": False, "message": 'Please provide status'}, status=status.HTTP_400_BAD_REQUEST
            )
        if not contract_status in ['pending', 'internal_approved', 'other_party_approved', 'rejected']:
            return Response(
                {"status": False,
                 "message": f"Status must be one of the following 'pending','internal_approved','other_party_approved','rejected' not {contract_status}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if contract_status == 'pending':
            queryset = User.objects.get(id=self.request.user.id).contract_reviewer.filter(status=contract_status)
        elif contract_status == 'internal_approved':
            queryset = User.objects.get(id=self.request.user.id).recieved_contract.filter(status=contract_status)

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

    def get(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        try:
            email = request.GET.get('email', None)
            if email:
                instance = Contract.objects.filter(id=kwargs["pk"])
                if instance:
                    valid_approvers = [inst.email for inst in instance[0].other_party_user.all() ]
                    user_approved_con = [inst.email for inst in instance[0].user_approved.all()]

                    user_rejected_con = [inst.email for inst in instance[0].user_rejected.all()]

                    valid_reviewers = [inst.email for inst in instance[0].reviewer_user.all()]
                    user_reviewed_con = [inst.email for inst in instance[0].user_reviewed.all()]

                    valid_approvers.extend(instance[0].non_registered_other_party_user)
                    user_approved_con.extend(instance[0].non_registered_user_approved)

                    valid_reviewers.extend(instance[0].non_registered_reviewer_user)
                    user_reviewed_con.extend(instance[0].non_registered_user_reviewed)

                    user_rejected_con.extend(instance[0].rejected_by)

                    serializer = self.get_serializer(instance[0])

                    if (email in valid_approvers and instance[0].status=='internal_approved') or (email in valid_reviewers and instance[0].status=='pending'):
                        return Response({"status": True, "data": serializer.data, "type": 'ARRIVED'},
                                        status=status.HTTP_200_OK)
                    elif (email in user_approved_con and instance[0].status=='other_party_approved') or (email in user_reviewed_con and instance[0].status=='internal_approved'):
                        return Response({"status": True, "data": serializer.data, "type": 'APPROVED'},
                                        status=status.HTTP_200_OK)
                    elif (email in user_rejected_con and instance[0].status in ['reviewer_rejected','other_party_rejected']):
                        return Response({"status": True, "data": serializer.data, "type": 'REJECTED'},
                                        status=status.HTTP_200_OK)

                    elif email in [instance[0].created_by.email]:
                        return Response({"status": True, "data": serializer.data, "type": 'OWNER'},
                                        status=status.HTTP_200_OK)
                    else:
                        return Response({"status": False, "message": 'invalid email provided'},
                                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"status": False, "message": "contract not found"},
                                    status=status.HTTP_204_NO_CONTENT)
            else:
                instance = Contract.objects.get(id=kwargs["pk"])
                serializer = self.get_serializer(instance)
                return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"status": False, "message": "contract not found"}, status=status.HTTP_204_NO_CONTENT)


    def update(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        user_approved_ids,user_approved_emails, user_reviewed_ids,user_reviewed_mails, user_rejected_ids,user_rejected_email = [], [], [], [], [], []
        updated_contract = request.data.get('upload',None)
        update_contract_date = request.data.get('contract_update_date',None)

        if updated_contract and not update_contract_date:
            request.data['contract_update_date'] = datetime.today().date().strftime("%Y-%m-%d")

        partial = kwargs.pop("partial", False)
        try:
            instance = Contract.objects.get(id=kwargs["pk"])
            valid_approvers = [inst.id for inst in instance.other_party_user.all()]
            valid_reviewers = [inst.id for inst in instance.reviewer_user.all()]
        except Exception as ex:
            logging.exception(f"exception in fetcing instance {ex}")
            return Response(
                {"status": False, "data": []}, status=status.HTTP_204_NO_CONTENT
            )
        valid_approvers_mail = [inst.email for inst in instance.other_party_user.all()]
        valid_non_registered_approvers = instance.non_registered_other_party_user
        valid_reviewers_email = [inst.email for inst in instance.reviewer_user.all()]
        requester_email = request.data.get('emails',None)
        requesting_status = request.data.get('status',None)

        if requester_email:
            for email in requester_email:
                if User.objects.filter(email=email):
                    if email in valid_approvers_mail:
                        if requesting_status == 'ACCEPTED':
                            user_approved_ids.append(User.objects.filter(email=email)[0].id)
                        elif requesting_status == 'REJECTED':
                            user_rejected_ids.append(User.objects.filter(email=email)[0].id)
                    elif email in valid_reviewers_email:
                        if requesting_status == 'ACCEPTED':
                            user_reviewed_ids.append(User.objects.filter(email=email)[0].id)
                        elif requesting_status == 'REJECTED':
                            user_rejected_ids.append(User.objects.filter(email=email)[0].id)
                    else:
                        pass
                else:
                    if email in valid_non_registered_approvers:
                        if requesting_status == 'ACCEPTED':
                            user_approved_emails.append(email)
                        elif requesting_status == 'REJECTED':
                            user_rejected_email.append(email)

                    elif email in valid_reviewers_email:
                        if requesting_status == 'ACCEPTED':
                            user_reviewed_mails.append(email)
                        elif requesting_status == 'REJECTED':
                            user_rejected_email.append(email)
                    else:
                        pass
            if user_approved_ids:
                request.data['user_approved'] = user_approved_ids
            if user_reviewed_ids:
                request.data['user_reviewed'] = user_reviewed_ids
            if user_approved_emails:
                request.data['non_registered_user_approved'] = user_approved_emails
            if user_reviewed_mails:
                request.data['non_registered_user_reviewed'] = user_reviewed_mails
            if user_rejected_ids:
                request.data['user_rejected'] = user_rejected_ids
            if user_rejected_email:
               request.data['rejected_by'] = user_rejected_email

        del request.data['emails']
        del request.data['status']

        serializer = self.serializer_class(
            instance, data=request.data, partial=partial,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.update(serializer.instance,serializer.validated_data)
            serializer.remove_user(request,serializer.instance,valid_approvers,valid_reviewers)
            Contract.update_internal_approval_status(serializer.instance)
            Contract.update_other_party_approval_status(serializer.instance)
            mail_sent, msg = serializer.mail_contract_agreement_link(serializer.instance)
            if mail_sent:
                logging.info(msg)
            else:
                logging.info(msg)
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

class DeleteFileS3(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        base_url = "https://e-contract-private.s3-ap-southeast-1.amazonaws.com/"
        file_urls = request.data.get("link", None)
        try:
            if file_urls:
                prefixes = [{'key':file_url.split(base_url)[-1]} for file_url in file_urls]
                delete_file(prefixes=prefixes)
                return Response({"status": True, "message": "File deleted Successfully"},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"status": False, "message": "No link Found to delete"},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status": False, "message": e},
                            status=status.HTTP_400_BAD_REQUEST)

class ListFileS3(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        prefix = request.data.get("prefix", None)
        try:
            if prefix:
                objs = listbucketfile(prefix)
                if objs:
                    return Response({"status": True, "data": objs},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({"status": True, "message": "empty folder"},
                                    status=status.HTTP_200_OK)

            else:
                return Response({"status": False, "message": "folder link not provided"},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status": False, "message": e},
                            status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = User.objects.get(id=request.user.id)
            serializer = self.get_serializer(instance)
            return Response(
                {"status": True, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            logging.exception(f"exception in fetcing instance {e}")
            return Response({"status": False, "message": e})
