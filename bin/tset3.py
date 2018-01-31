from collections import defaultdict

from src.models import friendfindermatch

matchmatcherlist = list(friendfindermatch.objects.values_list("matcher", flat=True))
matchmatcheelist = list(friendfindermatch.objects.values_list("matchee", flat=True))
currentsocialaccount = "2451520528295457"
# Get one way match, then search or other way match.
# GET ALL FB ACCOUNTS THAT ARE PASSABLE set(a) & set(b)

# Init user mutuality dict
newsocaccs = []
temp = defaultdict(list)
for delvt, pin in zip(matchmatcherlist, matchmatcheelist):
    if not temp[delvt].__contains__(pin):
        temp[delvt].append(pin)

# weed out mutuals TODO THIS DOSENT WEEK OUT MUTUALS; IT EXTRACTS THE SUBARRAY continue confobj down
confobj = []
for i in temp[currentsocialaccount.uid]:
    for j in temp[i]:
        if currentsocialaccount.uid == j:
            if not confobj.__contains__(i):
                confobj.append(i)

# delete self from mutual list
try:
    confobj.remove(currentsocialaccount.uid)
except:
    pass

# conver to socialaccount
passableobjects = []
for i in temp[currentsocialaccount.uid]:
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
             "confirmedmatcheslen": passableobjects.__len__(),
             }
)
