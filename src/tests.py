from django.test import TestCase
from src.models import User, fruitVote, fruitPerson, Munnygroup


# Create your tests here.
class fruitVoteTestClass(TestCase):
    def setUp(self):
        a_record = Munnygroup(groupname="Debate1")
        a_record.save()
        b_record = Munnygroup(groupname="Exec1")
        b_record.save()


    def test_userCreation(self):
            testuserone = User(Firstname="Benjamin",
                               Lastname="Rasmussen",
                               rolegroup_primary=Munnygroup.objects.get(groupname="Debate1"),
                               rolegroup_secondary=Munnygroup.objects.get(groupname="Exec1"))
            testuserone.save()


"""
    # Award for ugliest piece of code i ever wrote to date.
    fruitPerson.objects.get(userobject=User.objects.get(Firstname="Benjamin")).vote(fruitPerson.objects.get(userobject=User.objects.get(Firstname="Iustin")), False)
 """
