from __future__ import unicode_literals
import math
import uuid
from collections import defaultdict
from logging import exception

from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db import models
# Create your models here.
from django.dispatch import receiver


class Munnygroup(models.Model):
    groupname = models.CharField(help_text="Group name (exec or debate)", max_length=25)

    list_display = ('groupname',)
    fields = ('groupname',)

    def __str__(self):
        return str(self.groupname)


class munnyuser(models.Model):
    # TODO ADD PICTURE URL
    id = models.AutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='ID')
    Firstname = models.CharField(help_text="First name, (only 1, no spaces!)", max_length=20)
    Lastname = models.CharField(help_text="Last name, (only 1, no spaces!)", max_length=20)
    # FACEBOOKURL = models.
    # TODO Scrap groups for choices and groups
    rolegroup_primary = models.ForeignKey(Munnygroup, related_name="rolegroup_secondary", default="", )
    rolegroup_secondary = models.ForeignKey(Munnygroup, related_name="rolegroup_primary", default="", )

    MUNID = models.CharField(help_text="This is the google docs jotform id thingy", default="", max_length=20)

    FACEBOOKLINK = models.CharField(help_text="Facebbok ID", max_length=100)

    list_display = ('id', 'MUNID', 'Firstname', 'Lastname', 'rolegroup_primary', 'rolegroup_secondary',)
    fields = ('Firstname', 'Lastname', 'rolegroup_primary', 'rolegroup_secondary', 'MUNID')

    def __str__(self):
        return str(self.MUNID)

    def getfullname(self):
        return self.Firstname + " " + self.Lastname

    def getscore(self):
        try:
            score = 0
            svar = fruitVote.objects.filter(voter=self)
            countries = list(speakerCountry.objects.all())

            contdict = defaultdict(list)
            for i in countries:
                for j in svar:
                    if j.votee.country == i.country:
                        contdict[i.country].append(j.bool)

            truthlist = []
            for i in countries:
                truthlist.append(contdict[i.country][-1])

            for i, j in zip(truthlist, countries):
                if i == j.fruitsentiment:
                    score += 1

            return score
        except:
            return 0

    def __abs__(self):
        try:
            return self.getscore()
        except:
            return 0

    def __lt__(self, other):
        try:
            return self.getscore() < other.number
        except:
            return 0


class fruitPerson(models.Model):
    userobject = models.ForeignKey(munnyuser, default="")
    score = models.IntegerField(help_text="Display the score for the user linked",
                                default=0)
    # Scrap the fruitscore idea. let score be a request context that is returned by a function in this class.
    # such that you can track your score live as you vote.
    fruitbool = models.BooleanField(help_text="Used to keep track of wether or not the user linked has said fruitful",
                                    default=False, )
    """
    # TODO add speaker countries and country flags for the fruitvote's spake
    speakerbool = models.BooleanField(help_text="Is this person a speaker?",
                                      default=False,)
    """

    list_display = ('id', 'userobject', 'score', 'fruitbool')
    fields = ('userobject', 'fruitbool')

    def vote(self, otherperson, bool):
        fruitVote.create(self, otherperson, bool)

    @staticmethod
    def getscore(fruitPerson):
        # TODO assert fruitPerson
        fruitscore = 0
        # TODO implement livredder code for this bit
        return fruitscore


class speakerCountry(models.Model):
    country = models.CharField(max_length=35, help_text="Name of the conutry speaking right here")
    countryflag = models.CharField(max_length=100,
                                   help_text="URL for anchor links. Can be /src/static/images/country/<COUNTRYNAME>.png",
                                   default="/src/static/images/country/BLANK.png")
    fruitsentiment = models.BooleanField(help_text="Change this sentiment after the fact", default=None)

    list_display = ('id', 'country', 'countryflag', 'fruitsentiment')
    fields = ('country', 'countryflag', 'fruitsentiment',)

    def __str__(self):
        return self.country



class fruitVote(models.Model):
    voter = models.ForeignKey(munnyuser, related_name="votee")
    votee = models.ForeignKey(speakerCountry, related_name="voter")
    bool = models.BooleanField(help_text="Indicates what the voter voted", default=True)

    list_display = ('id', 'voter', 'votee', 'bool')
    fields = ('voter', 'votee', 'bool')

    @staticmethod
    def create(fvoter, fvotee, fbool):
        a_record = fruitVote(voter=fvoter, votee=fvotee, bool=fbool)
        a_record.save()


class ticket(models.Model):
    Title = models.CharField(max_length=50, help_text="Title of ticket goes here")
    Text = models.TextField(help_text="Simply the body of the ticket.")
    Writer = models.ForeignKey(munnyuser)
    InitDate = models.DateTimeField(auto_now=True, help_text="Date and time of creation")

    list_display = ('id', 'Title', 'InitDate', 'Text', 'Writer',)
    fields = ('Title', 'Text')

    def __str__(self):
        return str(self.id)


class ticketreply(models.Model):
    Text = models.TextField(help_text="Simply the body of the ticket.")
    InitDate = models.DateTimeField(auto_now=True, help_text="Date and time of creation")
    Writer = models.ForeignKey(munnyuser)
    Ticket = models.ForeignKey(ticket)

    list_display = ('id', 'Ticket', 'Writer', 'InitDate', 'Text')
    fields = ('Title', 'Text')

    def __str__(self):
        return str(self.id)


@receiver(models.signals.post_save, sender=munnyuser)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        # TODO Add clause such that not everyone is displayed as a speaker but everyone is a voter.

        record = fruitPerson(userobject=munnyuser.objects.last())
        record.save()

# TODO Make an @receiver that scans for a 'complementary' tinder match every time one is created.
