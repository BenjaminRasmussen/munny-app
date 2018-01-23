from __future__ import unicode_literals
import math
import uuid
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


class User(models.Model):
    # TODO ADD PICTURE URL
    Firstname = models.CharField(help_text="First name, (only 1, no spaces!)", max_length=20)
    Lastname = models.CharField(help_text="Last name, (only 1, no spaces!)", max_length=20)

    # FACEBOOKURL = models.

    # TODO Scrap groups for choices and groups
    rolegroup_primary = models.ForeignKey(Munnygroup, related_name="rolegroup_secondary", default="", )
    rolegroup_secondary = models.ForeignKey(Munnygroup, related_name="rolegroup_primary", default="", )

    jotformspace = models.CharField(help_text="This is the google docs jotform id thingy", max_length=20)

    list_display = ('id', 'jotformspace', 'Firstname', 'Lastname', 'rolegroup_primary', 'rolegroup_secondary',)
    fields = ('Firstname', 'Lastname', 'rolegroup_primary', 'rolegroup_secondary', 'jotformspace')

    def __str__(self):
        return str(self.id)

    def getfullname(self):
        return self.Firstname + " " + self.Lastname


class fruitPerson(models.Model):
    userobject = models.ForeignKey(User, User.objects.last())
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
                                   help_text="URL for anchor links. Can be /src/static/images/<COUNTRYNAME>.png")
    fruitsentiment = models.BooleanField(help_text="Change this sentiment after the fact", default=None)


class fruitVote(models.Model):
    voter = models.ForeignKey(fruitPerson, related_name="votee", default="")
    votee = models.ForeignKey(fruitPerson, related_name="voter", default="")
    bool = models.BooleanField(help_text="Indicates what the voter voted", default=None)

    list_display = ('id', 'voter', 'votee', 'bool')
    fields = ('voter', 'votee', 'bool')

    @staticmethod
    def create(fvoter, fvotee, fbool):
        a_record = fruitVote(voter=fvoter, votee=fvotee, bool=fbool)
        a_record.save()


@receiver(models.signals.post_save, sender=User)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        # TODO Add clause such that not everyone is displayed as a speaker but everyone is a voter.

        record = fruitPerson(userobject=User.objects.last())
        record.save()

# TODO Make an @receiver that scans for a 'complementary' tinder match every time one is created.




