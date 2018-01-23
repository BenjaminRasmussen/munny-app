from django.test import TestCase
from src.models import MUser, fruitVote, fruitPerson, Munnygroup

"""
    # Award for ugliest piece of code i ever wrote to date.
    fruitPerson.objects.get(userobject=User.objects.get(Firstname="Benjamin")).vote(fruitPerson.objects.get(userobject=User.objects.get(Firstname="Iustin")), False)
 """
