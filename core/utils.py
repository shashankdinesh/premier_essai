from rest_framework_simplejwt.tokens import RefreshToken
from core.models import User
import boto3, os

import logging
from django.core.mail import send_mail, EmailMessage
import json, requests, logging

import base64
import os
from sendgrid.sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail,
    Attachment,
    FileContent,
    FileName,
    FileType,
    Disposition,
    ContentId,
)





def get_tokens_for_user(user):
    #import pdb;pdb.set_trace()
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)
    return {
        "refresh": refresh_token,
        "access": access_token,
    }

def refresh_tokens_for_user(refresh_token):
    refresh = RefreshToken(refresh_token)

    # Change access token with same refresh token
    # access_token = str(refresh.access_token)
    # tokens = {
    #     'refresh': str(refresh),
    #     'access': access_token,
    # }

    # change refresh token each time access token change
    user = User.objects.get(id=refresh.get('user_id'))
    refresh.blacklist()
    tokens = get_tokens_for_user(user)
    return tokens

def send_email(
    from_email,
    to_emails,
    email_subject,
    html_content,
    pdf_file_name=None,
    pdf_file=None,
    sender_name="",
):

    if "123456@gmail.com" in to_emails:
        return

    if type(to_emails) == str:
        to_emails = [to_emails]

    message = Mail(
        from_email=(from_email, sender_name),
        to_emails=to_emails,
        subject=email_subject,
        html_content=html_content,
    )
    if pdf_file:
        # base64File = base64.b64encode(requests.get(pdf_file.url).content).decode()
        # attachment = Attachment()
        # attachment.file_content = FileContent(base64File)
        # attachment.file_type = FileType('application/pdf')
        # attachment.file_name = FileName(pdf_file_name)
        # attachment.disposition = Disposition('attachment')
        # attachment.content_id = ContentId('Example Content ID')
        # message.attachment = attachment

        attachment = Attachment()
        if ".csv" in pdf_file_name:
            base64File = base64.b64encode(pdf_file).decode()
            attachment.file_type = FileType("text/csv")
        else:

            base64File = base64.b64encode(requests.get(pdf_file).content).decode()
            attachment.file_type = FileType("application/pdf")

        attachment.file_content = FileContent(base64File)
        attachment.file_name = FileName(pdf_file_name)
        attachment.disposition = Disposition("attachment")
        attachment.content_id = ContentId("Example Content ID")
        message.attachment = attachment
    try:
        sendgrid_client = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sendgrid_client.send(message)
        logging.info(f"Email sent from sendgrid status {response.status_code}")

    except Exception as e:
        logging.info(
            "===========================Send email Error======================"
        )
        logging.info(e)
        logging.info(
            "======================================================================"
        )
        return False
    # logging.info(response.status_code)
    # logging.info(response.body)
    # logging.info(response.headers)
    return True


def upload_contract(filepath,filename):
    try:
        #import pdb;pdb.set_trace()
        resource = boto3.resource(
            "s3",
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
            region_name=os.environ.get("AWS_REGION"),
        )
        logging.info(f"resource created syccessfully")
        bucket = resource.Bucket("e-contract-private")
        prefix = f"contract/{filename}"
        bucket.upload_fileobj(filepath, prefix)
        return "https://e-contract-private.s3-ap-southeast-1.amazonaws.com/"+prefix
    except Exception as e:
        logging.info(f"exception is as follows {e}")
        return False