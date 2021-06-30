import re

from django.db import transaction
from django_common.auth_backends import User
from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes

from core.models import Contract
from econtract import errors
from rest_framework.utils import model_meta

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

    def update(self, instance, validated_data):
        #import pdb;pdb.set_trace()
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            elif attr in ['non_registered_user_approved','non_registered_user_reviewed','rejected_by']:
                field = getattr(instance, attr)
                field.extend(value)
            else:
                setattr(instance, attr, value)

        instance.save()

        # Note that many-to-many fields are set after updating instance.
        # Setting m2m fields triggers signals which could potentially change
        # updated instance and we do not want it to collide with .update()
        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.add(value[0].id)

        return instance

    def remove_user(self, request, contract,valid_approvers,valid_reviewers):

        approving_user = request.data.get('user_approved', None)
        approving_reviewer = request.data.get('user_reviewed', None)
        non_registered_user_approved = request.data.get('non_registered_user_approved', None)
        non_registered_user_reviewed = request.data.get('non_registered_user_reviewed', None)
        contract_rejected_by = request.data.get('rejected_by', None)
        user_rejected_contract = request.data.get('user_rejected', None)

        if approving_user:
            for id in approving_user:
                contract.other_party_user.remove(User.objects.get(id=id))
        if approving_reviewer:
            for id in approving_reviewer:
                contract.reviewer_user.remove(User.objects.get(id=id))
        if non_registered_user_approved:
            for email in non_registered_user_approved:
                contract.non_registered_other_party_user.remove(email)
            contract.save()
        if non_registered_user_reviewed:
            for email in non_registered_user_reviewed:
                contract.non_registered_reviewer_user.remove(email)
            contract.save()
        if contract_rejected_by:
            for email in contract_rejected_by:
                try:
                    if email in contract.non_registered_reviewer_user:
                        contract.non_registered_reviewer_user.remove(email)
                        contract.status = 'rejected'
                        contract.save()
                    elif email in contract.non_registered_other_party_user:
                        contract.non_registered_other_party_user.remove(email)
                        contract.status = 'rejected'
                        contract.save()
                except:
                    pass
        if user_rejected_contract:
            for user_id in user_rejected_contract:
                if user_id in valid_approvers:
                    contract.other_party_user.remove(User.objects.get(id=user_id))
                    contract.status = 'rejected'
                    contract.save()
                elif user_id in valid_reviewers:
                    contract.reviewer_user.remove(User.objects.get(id=user_id))
                    contract.status = 'rejected'
                    contract.save()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField()
    email = serializers.EmailField(required=False)

    def update_contracts_details(self,registered_user):
        try:
            contracts = Contract.objects.all()
            for contract in contracts:
                if registered_user.email in contract.non_registered_other_party_user:
                    contract.other_party_user.add(registered_user.id)
                if registered_user.email in contract.non_registered_reviewer_user:
                    contract.reviewer_user.add(registered_user.id)
                if registered_user.email in contract.non_registered_user_approved:
                    contract.user_approved.add(registered_user.id)
                if registered_user.email in contract.non_registered_user_reviewed:
                    contract.user_reviewed.add(registered_user.id)
                if registered_user.email in contract.rejected_by:
                    contract.user_rejected.add(registered_user.id)
            return True
        except:
            return False



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
