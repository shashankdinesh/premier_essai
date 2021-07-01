from rest_framework_simplejwt.tokens import RefreshToken
from core.models import User
import boto3, os
from django.conf import settings
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


def get_bucket():
    resource = boto3.resource(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        region_name=os.environ.get("AWS_REGION"),
    )
    bucket = resource.Bucket("e-contract-private")
    return bucket

def upload_contract(filepath,filename):
    try:
        #import pdb;pdb.set_trace()

        logging.info(f"resource created syccessfully")

        prefix = f"contract/{filename}"
        bucket = get_bucket()
        bucket.upload_fileobj(filepath, prefix)
        return "https://e-contract-private.s3-ap-southeast-1.amazonaws.com/"+prefix
    except Exception as e:
        logging.info(f"exception is as follows {e}")
        return False

def delete_file(prefixes):
    bucket = get_bucket()
    for prefix in prefixes:
        logging.info(f"*********** Deleting file link for {prefix['key']} ****************************")
        for obj in bucket.objects.filter(Prefix=prefix['key']):
            if obj.key==prefix['key']:
                obj.delete()
                logging.info(f"{prefix['key']} deleted")
            else:
                logging.info(f"{prefix['key']} not found")

def delete_contract_data(prefixes):
    try:
        s3_resource = boto3.resource(
            "s3",
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
            region_name=os.environ.get("AWS_REGION"),
        )
        print(prefixes)
        s3_resource.meta.client.delete_objects(Bucket='e-contract-private', Delete={'Objects': prefixes})
        return True
    except:
        return False


def listbucketfile(prefix):
    #import pdb;pdb.set_trace()
    obj_list=[]
    try:
        bucket = get_bucket()
        for obj in bucket.objects.filter(Prefix=prefix):
            print(obj.key)
            if not obj.key==prefix:
                obj_list.append(obj.key)
        return obj_list
    except:
        return False


def contract_mail_body(senders_mail_id, file_url, confirmation_url, expiration_date, register_url):
    msg_body = f"""Hi,<br>
                <br>
                書類の確認依頼が届きました。<br>

                ご確認をお願いいたします。

                <br>
                <br>
                <br>
                -----------------------------------------------------------<br>
                <br>
                ・送信元メールアドレス：{senders_mail_id}<br>
                ・書類名： {file_url}<br>
                ・確認用URL： {confirmation_url}<br>
                ・URL有効期限： {expiration_date}<br>
                <br>
                <br>

                有効期限を過ぎてしまった場合は送信者に再配信を依頼してください。<br>
                <br>
                <br>
                -----------------------------------------------------------<br>
                <br>
                本メールは送信専用のため、ご返信に対応する事はできません。<br>
                本メールに心あたりがない場合は削除をお願いいたします。<br>
                誤送付のメールを開示したり、自己利用のために用いることを固く禁じます。<br>
                <br>
                <br>
                無料会員登録は、こちらから<br>
                {register_url}<br>
               <br>
               <br>
                -----------------------------------------------------------<br><br>
                ＊クラウドコントラクトの推奨ブラウザはGoogle Chromeとなっております。<br>"""

    #suject = f"【社内確認】「{}」の確認依頼が届いております"
    return msg_body


def check_user_validity(approving_user,approving_reviewer,non_registered_user_approved,non_registered_user_reviewed,contract_rejected_by,instance,valid_approvers,valid_reviewers):

    if approving_user:
        for user in approving_user:
            if not user in valid_approvers:
                return {"status": False,
                     "message": f"approving user {user} is not in other party user list {valid_approvers}"}


    if approving_reviewer:
        for user in approving_reviewer:
            if not user in valid_reviewers:
                return {"status": False, "message": f"Reviewing user {user} is not in Review user list {valid_reviewers}"}

    if non_registered_user_approved:
        for non_registered_user in non_registered_user_approved:
            if not non_registered_user in instance.non_registered_other_party_user:
                return {"status": False,
                     "message": f"{non_registered_user} is not in non registered other party user list {instance.non_registered_other_party_user}"}

    if non_registered_user_reviewed:
        for non_registered_reviewer in non_registered_user_reviewed:
            if not non_registered_reviewer in instance.non_registered_reviewer_user:
                return {"status": False,
                     "message": f"{non_registered_reviewer} is not in non registered other party user list {instance.non_registered_reviewer_user}"}


    if contract_rejected_by:
        try:
            user = User.objects.get(email=contract_rejected_by)
            if not user in valid_approvers and not user in valid_reviewers:
                return {"status": False,
                "message": f"{user} is neither other party user or reviewer"}
        except:
            if not contract_rejected_by in instance.non_registered_reviewer_user and not contract_rejected_by in instance.non_registered_other_party_user:
                return {"status": False,
                        "message": f"{contract_rejected_by} is neither in non registered reviewer nor in non registered other party users"}





