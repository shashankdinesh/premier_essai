import os

import datetime
from collections import Counter

from django.core.management.base import BaseCommand

from core.models import Contract
import logging


class Command(BaseCommand):
    help = "Update Contract Status"


    def handle(self, *args, **options):
        try:
            contracts = Contract.objects.all()
            for contract in contracts:
                other_party_users = contract.other_party_user.all()
                reviewer_users = contract.reviewer_user.all()
                approved_users = contract.user_approved.all()
                reviewed_user = contract.user_reviewed.all()
                if Counter(other_party_users) == Counter(approved_users) and Counter(reviewer_users) == Counter(
                        reviewed_user):
                    contract.status = "approved"
                    contract.save()
        except Exception as e:
            print(e)
            logging.exception(f''' Exception: {e} found while updating contract status''')
            pass
