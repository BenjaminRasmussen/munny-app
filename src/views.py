import json
from collections import defaultdict

from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.facebook.provider import FacebookProvider, GRAPH_API_URL
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from src.models import munnyuser, fruitPerson, speakerCountry, ticket, ticketreply, Munnygroup, fruitVote, \
    friendfindermatch
from allauth import socialaccount


# Create your views here.

def index(request):
    return render(
        request,
        'index.html',
        context={"user_name": "user_name"}
    )


def fruit(request):
    userid = request.session.get('munnyid', 'NOT LOGGED IN')
    if not userid == "NOT LOGGED IN":
        Username = munnyuser.objects.get(MUNID=userid).getfullname()
    else:
        return HttpResponseRedirect('/missingloginpage/')

    curUser = munnyuser.objects.get(MUNID=request.session.get('munnyid'))
    """
    if request.method == "POST":
        # Get some of those answers! System works like this. POST returns a list of countries.
        # If a country is in that list. then the person voted fruitful for said country. GL!
        countrylist = request.POST.getlist('CHECKER')
        for i in list(speakerCountry.objects.all()):
            if i.country in countrylist:
                t = fruitVote.objects.create(
                    voter=curUser,
                    votee=i,
                    bool=True,
                )
                t.save()
            else:
                t = fruitVote.objects.create(
                    voter=curUser,
                    votee=i,
                    bool=False,
                )
                t.save()

        return render(request,
                      'successfullPostPage.html',
                      context={"user_name": Username,
                               "fruit_object": fruitPerson.objects.get(userobject=munnyuser.objects.get(MUNID=userid))},
                      )
    """
    # Return default values
    votes = fruitVote.objects.filter(voter=curUser).order_by('votee_id')
    countrydict = {}
    for i in list(speakerCountry.objects.all()):
        for j in votes:
            if i.id == j.votee.id:
                try:
                    countrydict[str(i.country)] = j.bool
                except:
                    pass
    a = []
    for i in list(speakerCountry.objects.all()):
        try:
            if countrydict[str(i.country)]:
                a.append(i.country)
        except:
            pass

    return render(
        request,
        'fruitvote.html',
        context={"user_name": Username,
                 "fruitpersons": speakerCountry.objects.all(),
                 "countrylistwithtrue": a,
                 },
    )


def fruitleader(request):
    userid = request.session.get('munnyid', 'NOT LOGGED IN')
    if not userid == "NOT LOGGED IN":
        Username = munnyuser.objects.get(MUNID=userid).getfullname()
    else:
        return HttpResponseRedirect('/missingloginpage/')

    scorelist = []
    fruitlist = munnyuser.objects.all()
    for i in fruitlist:
        try:
            scorelist.append(i)
        except:
            pass
    from operator import methodcaller
    scorelist = sorted(scorelist, key=lambda obj: obj.getscore(), reverse=True)

    return render(
        request,
        'fruitleaderboard.html',
        context={"user_name": Username,
                 "leaderboard": scorelist},

    )


def ticketview(request):
    ticketreplies = list(ticketreply.objects.all())

    userid = request.session.get('munnyid', 'NOT LOGGED IN')
    if not userid == "NOT LOGGED IN":
        Username = munnyuser.objects.get(MUNID=userid).getfullname()
    else:
        return HttpResponseRedirect('/missingloginpage/')

    if request.method == "POST":

        # Checking if its a reply to a post by ad-staff
        if 'reply' and 'ticketobject' in request.POST:
            curUser = munnyuser.objects.get(MUNID=request.session.get('munnyid'))
            repliedtickettarget = ticket.objects.get(id=request.POST['ticketobject'])
            replytext = request.POST['reply']
            t, created = ticketreply.objects.get_or_create(Writer=curUser,
                                                           Text=replytext,
                                                           Ticket=repliedtickettarget,
                                                           )

            t.save()

        # Checking if its a ticket post
        if 'title' and 'besked' in request.POST:
            curUser = munnyuser.objects.get(MUNID=request.session.get('munnyid'))
            title = request.POST['title']
            bodytext = request.POST['besked']
            t, created = ticket.objects.get_or_create(Writer=curUser,
                                                      Title=title,
                                                      Text=bodytext,
                                                      )

            t.save()

        return render(request,
                      'successfullPostPage.html',
                      context={"user_name": Username},
                      )

    curUser = munnyuser.objects.get(MUNID=request.session.get('munnyid'))
    if ticket.objects.filter(Writer=curUser):
        tickets = ticket.objects.filter(Writer=curUser).order_by('InitDate').reverse()
    else:
        tickets = {}

    # TODO clean this section with role choices instead of group models.

    if request.method == "GET" and curUser.rolegroup_primary == munnyuser.ADSTAFF:
        tickets = ticket.objects.all().order_by('InitDate').reverse()
        return render(request,
                      'ticketreader.html',
                      context={"user_name": Username,
                               "tickets": tickets,
                               "ticketreplies": ticketreplies,
                               },
                      )

    else:
        return render(
            request,
            'ticketwriter.html',
            context={"user_name": Username,
                     "tickets": tickets,
                     "ticketreplies": ticketreplies,
                     },
        )


def sessionsview(request):
    GetText = str(request.get_raw_uri()).split("/")
    GetText = GetText[-1]
    print(GetText)
    request.session['munnyid'] = str(GetText)
    return HttpResponseRedirect('/src/')


@login_required
def friendfinderview(request):
    if request.user.is_authenticated():
        user = request.user
    userid = request.session.get('munnyid', 'NOT LOGGED IN')
    if not userid == "NOT LOGGED IN":
        Username = munnyuser.objects.get(MUNID=userid).getfullname()
    else:
        return HttpResponseRedirect('/missingloginpage/')

    socaccs = SocialAccount.objects.all()
    currentsocialaccount = SocialAccount.objects.get(user=request.user)

    # Get number of mutual matches
    confrimedmatches = []
    matchlist = list(friendfindermatch.objects.values_list("matcher", flat=True))
    for i in matchlist:
        try:
            if friendfindermatch.objects.get(matcher=i, matchee=currentsocialaccount.uid):
                confrimedmatches.append(friendfindermatch.objects.get(matcher=i, matchee=currentsocialaccount.uid))
                print(confrimedmatches)
            else:
                print(i)
                print(currentsocialaccount.uid)
        except:
            pass

    confirmedobjects = []
    matchobjectlist = friendfindermatch.objects.all()
    for i in matchobjectlist:
        try:
            confirmedobjects.append(friendfindermatch.objects.get(matcher=i.matchee, matchee=i.matcher))
        except:
            pass

    matchmatcherlist = list(friendfindermatch.objects.values_list("matcher", flat=True))
    matchmatcheelist = list(friendfindermatch.objects.values_list("matchee", flat=True))
    # Get one way match, then search or other way match.
    # GET ALL FB ACCOUNTS THAT ARE PASSABLE set(a) & set(b)

    # Init user mutuality dict
    newsocaccs = []
    temp = defaultdict(list)
    for delvt, pin in zip(matchmatcherlist, matchmatcheelist):
        if not temp[delvt].__contains__(pin) and delvt != pin:
            temp[delvt].append(pin)

    # weed out mutuals TODO THIS DOSENT WEEK OUT MUTUALS; IT EXTRACTS THE SUBARRAY continue confobj down
    confobj = []
    for i in temp[currentsocialaccount.uid]:
        for j in temp[i]:
            print("temp sublist i:"+ str(i) + str(temp[i]))
            if not confobj.__contains__(j):
                confobj.append(j)
    print(confobj)
    # delete self from mutual list
    try:
        confobj.remove(currentsocialaccount.uid)
    except:
        pass


    # conver to socialaccount
    passableobjects = []
    for i in confobj:
        passableobjects.append(SocialAccount.objects.get(uid=i))
    taccs = []

    for i in list(socaccs):
        if not list(passableobjects).__contains__(i):
            taccs.append(i)
    try:
        taccs.remove(currentsocialaccount)
    except:
        pass

    try:
        passableobjects.remove(currentsocialaccount)
    except:
        pass
    return render(
        request,
        'visual.html',
        context={"users": munnyuser.objects.all(),
                 "user_name": Username,
                 "facebookaccounts": taccs,
                 "currentFacebookAccount": currentsocialaccount,
                 "confirmedmatches": passableobjects,
                 "confirmedmatcheslen": confobj.__len__(),
                 }
    )


@login_required
def matchesview(request):
    if request.user.is_authenticated():
        user = request.user
    userid = request.session.get('munnyid', 'NOT LOGGED IN')
    if not userid == "NOT LOGGED IN":
        Username = munnyuser.objects.get(MUNID=userid).getfullname()
    else:
        return HttpResponseRedirect('/missingloginpage/')

    socaccs = SocialAccount.objects.all()
    currentsocialaccount = SocialAccount.objects.get(user=request.user)
    matchmatcherlist = list(friendfindermatch.objects.values_list("matcher", flat=True))
    matchmatcheelist = list(friendfindermatch.objects.values_list("matchee", flat=True))
    # Get one way match, then search or other way match.
    # GET ALL FB ACCOUNTS THAT ARE PASSABLE set(a) & set(b)
    # Init user mutuality dict
    newsocaccs = []
    temp = defaultdict(list)
    for delvt, pin in zip(matchmatcherlist, matchmatcheelist):
        if not temp[delvt].__contains__(pin) and delvt != pin:
            temp[delvt].append(pin)
    print(temp)
    # weed out mutuals
    confobj = []
    for i in temp[currentsocialaccount.uid]:
        for j in temp[i]:
            print("temp sublist i:"+ str(i) + str(temp[i]))
            if not confobj.__contains__(j):
                confobj.append(j)
    print(confobj)
    # delete self from mutual list
    try:
        confobj.remove(currentsocialaccount.uid)
    except:
        pass

    # conver to socialaccount
    passableobjects = []
    for i in confobj:
        passableobjects.append(SocialAccount.objects.get(uid=i))

    try:
        passableobjects.remove(currentsocialaccount)
    except:
        pass
    print(passableobjects)
    return render(request,
                  'matches.html',
                  context={"users": munnyuser.objects.all(),
                           "user_name": Username,
                           "facebookaccounts": socaccs,
                           "currentFacebookAccount": currentsocialaccount,
                           "confirmedmatches": passableobjects,
                           })


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


def suc(request):
    return render(
        request,
        'successfullPostPage.html'
    )


def creditsview(request):
    return render(
        request,
        'formal/credits.html'
    )


def TOSview(request):
    return render(
        request,
        'formal/TOS.html'
    )


def PricavyPolicyview(request):
    return render(
        request,
        'formal/Privacy_Policy.html'
    )


from django.shortcuts import *
from django.template import RequestContext


@csrf_exempt
def testview(request):
    currentsocialaccount = request.user

    if request.method == "POST":
        form = request.POST

        message = "HELLO WORLD"

        return HttpResponse(json.dumps({'message': message}))

    return render(request,
                  'test.html',
                  context={"currentuser": currentsocialaccount}
                  )


def friendfinderajaxcall(request):
    # Data passed on from the AJAX call
    matcher = request.GET['matcher']
    matchee = request.GET['matchee']

    fmatchee = SocialAccount.objects.get(uid=matchee)

    a = friendfindermatch.objects.create(matcher=matcher,
                                         matchee=matchee)
    a.save()

    print("matcher: " + str(matcher),
          "matchee: " + str(matchee),
          "fmatchee: " + str(fmatchee))

    response_data = {}
    try:
        if friendfindermatch.objects.get(matcher__exact=matchee,
                                                matchee__exact=matcher, ):
            response_data['matchee'] = str(fmatchee)
            response_data['getMatchStatus'] = "true"
            print(response_data)
        else:
            response_data['getMatchStatus'] = "false"
    except:
        pass
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def ajaxcallview(request):
    print("GOT IT")
    message = "HELLO WORLD"
    response_data = {}
    try:
        response_data['result'] = 'Success'
        response_data['message'] = message
    except:
        response_data['result'] = 'oh no!'
        response_data['message'] = "The subprocess module did not run the script correctly!"

    return HttpResponse(json.dumps(response_data), content_type="application/json")


# When account is created via social, fire django-allauth signal to populate Django User record.
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    '''
    When a social account is created successfully and this signal is received,
    django-allauth passes in the sociallogin param, giving access to metadata on the remote account, e.g.:

    sociallogin.account.provider  # e.g. 'twitter'
    sociallogin.account.get_avatar_url()
    sociallogin.account.get_profile_url()
    sociallogin.account.extra_data['screen_name']

    See the socialaccount_socialaccount table for more in the 'extra_data' field.
    '''
    if sociallogin:
        # Extract first / last names from social nets and store on User record

        if sociallogin.account.provider == 'facebook':
            user.first_name = sociallogin.account.extra_data['first_name']
            user.last_name = sociallogin.account.extra_data['last_name']

        user.save()
