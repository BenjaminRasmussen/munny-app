from django.contrib import admin
from src.models import User, Munnygroup, fruitPerson, fruitVote


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = User.list_display
    fields = User.fields


@admin.register(Munnygroup)
class MunnygroupAdmin(admin.ModelAdmin):
    list_display = Munnygroup.list_display
    fields = Munnygroup.fields


@admin.register(fruitPerson)
class fruitPersonAdmin(admin.ModelAdmin):
    list_display = fruitPerson.list_display
    fields = fruitPerson.fields


@admin.register(fruitVote)
class fruitVoteAdmin(admin.ModelAdmin):
    list_display = fruitVote.list_display
    fields = fruitVote.fields
