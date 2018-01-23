from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.facebook.provider import FacebookProvider, GRAPH_API_URL
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render

from src.models import User, fruitPerson
from allauth import socialaccount


# Create your views here.

def index(request):
    return render(
        request,
        'index.html',
        context={"user_name": "user_name"}
    )


def fruit(request):
    if request.method == "POST":
        print(request.POST)

    userid = request.session.get('munnyid', 'NOT LOGGED IN')
    if not userid == "NOT LOGGED IN":
        Username = User.objects.get(MUNID=userid).getfullname()
        return render(
            request,
            'fruitvote.html',
            context={"user_name": Username,
                     "fruitpersons": fruitPerson.objects.all(), },
        )
    else:
        return HttpResponseRedirect('/missingloginpage/')


def fruitleader(request):
    userid = request.session.get('munnyid', 'NOT LOGGED IN')
    if not userid == "NOT LOGGED IN":
        Username = User.objects.get(MUNID=userid).getfullname()
        return render(
            request,
            'fruitleaderboard.html',
            context={"user_name": Username},
        )
    else:
        return HttpResponseRedirect('/missingloginpage/')


def ticketview(request):
    if request.POST:
        print(request)
        # TODO make ticket!

    # User cookie
    userid = request.session.get('munnyid', 'NOT LOGGED IN')
    if not userid == "NOT LOGGED IN":
        Username = User.objects.get(MUNID=userid).getfullname()

        return render(
            request,
            'ticketwriter.html',
            context={"user_name": Username,
                     },
        )
    else:
        return HttpResponseRedirect('/missingloginpage/')


def sessionsview(request):
    GetText = str(request.get_raw_uri()).split("/")
    GetText = GetText[-1]
    print(GetText)
    request.session['munnyid'] = str(GetText)
    return HttpResponseRedirect('/src/')


@login_required
def friendfinderview(request):
    userid = request.session.get('munnyid', 'NOT LOGGED IN')
    if not userid == "NOT LOGGED IN":
        Username = User.objects.get(MUNID=userid).getfullname()
    else:
        Username = "NOT LOGGED IN"

    # GET ALL FB ACCOUNTS
    socaccs = SocialAccount.objects.all()
    return render(
        request,
        'visual.html',
        context={"users": User.objects.all(),
                 "user_name": Username,
                 "facebookaccounts": socaccs,
                 }
    )


def missingloginpage(request):
    return render(
        request,
        'PLEASELOGINPAGE.html',
    )


def fb_complete_login(request, app, token):
    provider = providers.registry.by_id(FacebookProvider.id)

    # Generate an appsecret_proof parameter to secure the Graph API call
    # see https://developers.facebook.com/docs/graph-api/securing-requests
    import hashlib, hmac
    _msg = bytes(token.token).encode('utf-8')
    _key = bytes(app.secret).encode('utf-8')
    appsecret_proof = hmac.new(_key, _msg, digestmod=hashlib.sha256).hexdigest()

    resp = requests.get(
        GRAPH_API_URL + '/me',
        params={
            'fields': ','.join(provider.get_fields()),
            'access_token': token.token,
            'appsecret_proof': appsecret_proof
        })

    resp.raise_for_status()
    extra_data = resp.json()
    login = provider.sociallogin_from_response(request, extra_data)
    return login
