#project/settings/adapter.py
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse,redirect
from allauth.account.models import EmailAddress
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.signals import social_account_added
from allauth.account.utils import perform_login
from django.dispatch import receiver
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from src.models import munnyuser


@receiver(social_account_added)
def link_to_local_user(sender, request, sociallogin, **kwargs):
    try:
        userid = request.session.get('munnyid')
        muser = munnyuser.objects.get(MUNID=userid)
        muser.FACEBOOKLINK = sociallogin.account
    except:
        pass