import re

from django.db import transaction
from django_common.auth_backends import User
from rest_framework import serializers
from core.models import Contract
from econtract import errors

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField()
    email = serializers.EmailField(required=False)

    def validate(self, attrs):
        # print(attrs);
        if not attrs.get("password") == attrs.pop("confirm_password"):
            raise serializers.ValidationError(errors.UR_PASS_AND_CONFRM_PASS_DONT_MATCH)

        username = attrs.get("username")
        if not re.match(r"^[a-zA-Z0-9\-\_.]*$", username):
            raise serializers.ValidationError(errors.USER_NAME_NOT_ALLOWED)
        return attrs

    @transaction.atomic()
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.is_active = True
        user.is_superuser = False
        user.save()

        return user

    class Meta:
        model = User
        fields = (
            "password",
            "username",
            "confirm_password",
            "first_name",
            "last_name",
            "email"
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "user_type"
        )
