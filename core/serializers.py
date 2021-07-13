import logging
import re

from django.db import transaction
from django_common.auth_backends import User
from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes

from core.models import Contract
from core.utils import contract_mail_body, getpresignedUrl, send_contract_email
from econtract import errors
from rest_framework.utils import model_meta
from django.core.mail import EmailMessage

class ContractSerializer(serializers.ModelSerializer):
    contract_link = serializers.SerializerMethodField()
    created_by_email = serializers.SerializerMethodField()
    other_part_user_mail = serializers.SerializerMethodField()
    other_part_user_approved_mail = serializers.SerializerMethodField()
    reviewer_mail = serializers.SerializerMethodField()
    user_reviewed_mail = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = "__all__"

    def get_contract_link(self, obj):
        link = getpresignedUrl(bucket='e-contract-private',key=f'contract/{obj.contract_name}')
        return link

    def get_created_by_email(self, obj):
        return obj.created_by.email

    def get_other_part_user_mail(self, obj):
        return [user.email for user in obj.other_party_user.all()]

    def get_reviewer_mail(self, obj):
        return [user.email for user in obj.reviewer_user.all()]

    def get_other_part_user_approved_mail(self, obj):
        return [user.email for user in obj.user_approved.all()]

    def get_user_reviewed_mail(self, obj):
        return [user.email for user in obj.user_reviewed.all()]

    def mail_contract_agreement_link(self, contract,expiration_date="28-08-2021"):
        d_mail_ids_opu = ", ".join([email for email in contract.non_registered_other_party_user])
        if d_mail_ids_opu:
            d_mail_ids= d_mail_ids_opu +', '+ ", ".join([user.email for user in contract.other_party_user.all()])
        else:
            d_mail_ids = ", ".join([user.email for user in contract.other_party_user.all()])
        msg_body, subject = contract_mail_body(
            senders_mail_id=contract.created_by.email,
            destination_mail_id=d_mail_ids,
            file_name=contract.contract_name,
            confirmation_url=f'https://econtract.cazicazi.com/page/preview/{contract.id}',
            expiration_date=contract.contract_expiry_date
        )
        user_already_sent_mail = contract.mail_sent
        non_registered_other_party_users = [mail_id for mail_id in contract.non_registered_other_party_user if
                                            not mail_id in user_already_sent_mail]
        non_registered_reviewer_users = [mail_id for mail_id in contract.non_registered_reviewer_user if
                                         not mail_id in user_already_sent_mail]
        other_party_users = [user.email for user in contract.other_party_user.all() if
                             not user.email in user_already_sent_mail]
        reviewer_users = [user.email for user in contract.reviewer_user.all() if
                          not user.email in user_already_sent_mail]
        reviewer_users.extend(non_registered_reviewer_users)
        other_party_users.extend(non_registered_other_party_users)
        if contract.status == 'pending':
            if reviewer_users:
                mail_sent = send_contract_email(
                    from_email=contract.created_by.email,
                    to_emails=reviewer_users,
                    email_subject=subject,
                    html_content=msg_body,
                    sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                )
                if mail_sent:
                    contract.mail_sent.extend(reviewer_users)
                    contract.save()
                    return True, "Mail send Successfully to all reviewers"
                else:
                    return False, "Sending Mail to all reviewers Failed "
            else:
                return True, "Mail already send to all reviewers"
        elif contract.status == 'internal_approved':
            if other_party_users:
                mail_sent = send_contract_email(
                    from_email=contract.created_by.email,
                    to_emails=other_party_users,
                    email_subject=subject,
                    html_content=msg_body,
                    sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                )
                if mail_sent:
                    contract.mail_sent.extend(other_party_users)
                    contract.save()
                    return True, "Mail send Successfully to all other party users"
                else:
                    return False, "Sending Mail to all other party users Failed "
            else:
                return True, "Mail already send to all other party users"
        else:
            return True, "Mail already send to all other party users"

    def update(self, instance, validated_data):
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
                user_app = User.objects.get(id=id)
                contract.other_party_user.remove(user_app)
                msg_body, subject = contract_mail_body(
                    senders_mail_id=contract.created_by.email,
                    file_name=contract.contract_name,
                    confirmation_url=f'https://econtract.cazicazi.com/page/preview/{contract.id}',
                    expiration_date=contract.contract_expiry_date,
                    #register_url=register_url,
                    mail_type = 'APPROVED',
                )

                mail_sent = send_contract_email(
                    from_email=contract.created_by.email,
                    to_emails=user_app.email,
                    email_subject=subject,
                    html_content=msg_body,
                    sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                )
                if mail_sent:
                    logging.info(f"mail sent to {user_app.email}")
                else:
                    logging.info(f"mail sent failed {user_app.email}")

        if approving_reviewer:
            for id in approving_reviewer:
                user_app_review = User.objects.get(id=id)
                contract.reviewer_user.remove(user_app_review)
                msg_body, subject = contract_mail_body(
                    senders_mail_id=contract.created_by.email,
                    file_name=contract.contract_name,
                    confirmation_url=f'https://econtract.cazicazi.com/page/preview/{contract.id}',
                    # expiration_date=expiration_date,
                    # register_url=register_url,
                    mail_type='APPROVED',
                )

                mail_sent = send_contract_email(
                    from_email=contract.created_by.email,
                    to_emails=user_app_review.email,
                    email_subject=subject,
                    html_content=msg_body,
                    sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                )
                if mail_sent:
                    logging.info(f"mail sent to {user_app_review.email}")
                else:
                    logging.info(f"mail sent failed {user_app_review.email}")


        if non_registered_user_approved:
            for email in non_registered_user_approved:
                contract.non_registered_other_party_user.remove(email)
                contract.save()
                msg_body, subject = contract_mail_body(
                    senders_mail_id=contract.created_by.email,
                    file_name=contract.contract_name,
                    confirmation_url=f'https://econtract.cazicazi.com/page/preview/{contract.id}',
                    # expiration_date=expiration_date,
                    # register_url=register_url,
                    mail_type='APPROVED',
                )

                mail_sent = send_contract_email(
                    from_email=contract.created_by.email,
                    to_emails=email,
                    email_subject=subject,
                    html_content=msg_body,
                    sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                )
                if mail_sent:
                    logging.info(f"mail sent to {email}")
                else:
                    logging.info(f"mail sent failed {email}")



        if non_registered_user_reviewed:
            #import pdb;pdb.set_trace()
            for email in non_registered_user_reviewed:
                contract.non_registered_reviewer_user.remove(email)
                contract.save()
                msg_body, subject = contract_mail_body(
                    senders_mail_id=contract.created_by.email,
                    file_name=contract.contract_name,
                    confirmation_url=f'https://econtract.cazicazi.com/page/preview/{contract.id}',
                    # expiration_date=expiration_date,
                    # register_url=register_url,
                    mail_type='APPROVED',
                )

                mail_sent = send_contract_email(
                    from_email=contract.created_by.email,
                    to_emails=email,
                    email_subject=subject,
                    html_content=msg_body,
                    sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                )
                if mail_sent:
                    logging.info(f"mail sent to {email}")
                else:
                    logging.info(f"mail sent failed {email}")



        if contract_rejected_by:
            for email in contract_rejected_by:
                try:
                    if email in contract.non_registered_reviewer_user:
                        contract.non_registered_reviewer_user.remove(email)
                        contract.status = 'reviewer_rejected'
                        contract.save()
                        msg_body, subject = contract_mail_body(
                            senders_mail_id=contract.created_by.email,
                            file_name=contract.contract_name,
                            confirmation_url=f'https://econtract.cazicazi.com/page/preview/{contract.id}',
                            # expiration_date=expiration_date,
                            # register_url=register_url,
                            mail_type='REJECTED',
                        )

                        mail_sent = send_contract_email(
                            from_email=contract.created_by.email,
                            to_emails=email,
                            email_subject=subject,
                            html_content=msg_body,
                            sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                        )
                        if mail_sent:
                            logging.info(f"mail sent to {email}")
                        else:
                            logging.info(f"mail sent failed {email}")


                    elif email in contract.non_registered_other_party_user:
                        contract.non_registered_other_party_user.remove(email)
                        contract.status = 'other_party_rejected'
                        contract.save()
                        msg_body, subject = contract_mail_body(
                            senders_mail_id=contract.created_by.email,
                            file_name=contract.contract_name,
                            confirmation_url=f'https://econtract.cazicazi.com/page/preview/{contract.id}',
                            # expiration_date=expiration_date,
                            # register_url=register_url,
                            mail_type='REJECTED',
                        )

                        mail_sent = send_contract_email(
                            from_email=contract.created_by.email,
                            to_emails=email,
                            email_subject=subject,
                            html_content=msg_body,
                            sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                        )
                        if mail_sent:
                            logging.info(f"mail sent to {email}")
                        else:
                            logging.info(f"mail sent failed {email}")

                except:
                    pass
        if user_rejected_contract:
            for user_id in user_rejected_contract:
                usr_rej = User.objects.get(id=user_id)
                if user_id in valid_approvers:
                    contract.other_party_user.remove(usr_rej)
                    contract.status = 'other_party_rejected'
                    contract.save()
                    msg_body, subject = contract_mail_body(
                        senders_mail_id=contract.created_by.email,
                        file_name=contract.contract_name,
                        confirmation_url=f'https://econtract.cazicazi.com/page/preview/{contract.id}',
                        # expiration_date=expiration_date,
                        # register_url=register_url,
                        mail_type='REJECTED',
                    )

                    mail_sent = send_contract_email(
                        from_email=contract.created_by.email,
                        to_emails=usr_rej.email,
                        email_subject=subject,
                        html_content=msg_body,
                        sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                    )
                    if mail_sent:
                        logging.info(f"mail sent to {usr_rej.email}")
                    else:
                        logging.info(f"mail sent failed {usr_rej.email}")
                elif user_id in valid_reviewers:
                    usr_rej_review = User.objects.get(id=user_id)
                    contract.reviewer_user.remove(usr_rej_review)
                    contract.status = 'reviewer_rejected'
                    contract.save()
                    msg_body, subject = contract_mail_body(
                        senders_mail_id=contract.created_by.email,
                        file_name=contract.contract_name,
                        confirmation_url=f'https://econtract.cazicazi.com/page/preview/{contract.id}',
                        # expiration_date=expiration_date,
                        # register_url=register_url,
                        mail_type='REJECTED',
                    )

                    mail_sent = send_contract_email(
                        from_email=contract.created_by.email,
                        to_emails=usr_rej_review.email,
                        email_subject=subject,
                        html_content=msg_body,
                        sender_name=contract.created_by.first_name + " " + contract.created_by.last_name
                    )
                    if mail_sent:
                        logging.info(f"mail sent to {usr_rej_review.email}")
                    else:
                        logging.info(f"mail sent failed {usr_rej_review.email}")


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=False)

    def update_contracts_details(self,registered_user):
        try:
            contracts = Contract.objects.all()
            for contract in contracts:
                if registered_user.email in contract.non_registered_other_party_user:
                    contract.other_party_user.add(registered_user.id)
                    contract.non_registered_other_party_user.remove(registered_user.email)
                    contract.save()
                if registered_user.email in contract.non_registered_reviewer_user:
                    contract.reviewer_user.add(registered_user.id)
                    contract.non_registered_reviewer_user.remove(registered_user.email)
                    contract.save()
                if registered_user.email in contract.non_registered_user_approved:
                    contract.user_approved.add(registered_user.id)
                    contract.non_registered_user_approved.remove(registered_user.email)
                    contract.save()
                if registered_user.email in contract.non_registered_user_reviewed:
                    contract.user_reviewed.add(registered_user.id)
                    contract.non_registered_user_reviewed.remove(registered_user.email)
                    contract.save()
                if registered_user.email in contract.rejected_by:
                    contract.user_rejected.add(registered_user.id)
                    contract.rejected_by.remove(registered_user.email)
                    contract.save()
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
        #import pdb;pdb.set_trace()
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.is_active = True
        user.is_superuser = False
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    class Meta:
        model = User
        fields = (
            "id",
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
        exclude = ('password','user_permissions','groups')
