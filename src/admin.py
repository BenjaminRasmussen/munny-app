from django.contrib import admin
from src.models import munnyuser, Munnygroup, fruitPerson, fruitVote, speakerCountry, ticket, ticketreply, \
    friendfindermatch


# Register your models here.


@admin.register(munnyuser)
class munnyuseradmin(admin.ModelAdmin):
    list_display = munnyuser.list_display
    fields = munnyuser.fields


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

@admin.register(speakerCountry)
class speakCountryAdmin(admin.ModelAdmin):
    list_display = speakerCountry.list_display
    fields = speakerCountry.fields


@admin.register(ticket)
class ticketAdmin(admin.ModelAdmin):
    list_display = ticket.list_display
    fields = ticket.fields


@admin.register(ticketreply)
class ticketreplyAdmin(admin.ModelAdmin):
    list_display = ticketreply.list_display
    fields = ticketreply.fields


@admin.register(friendfindermatch)
class friendfindermatch(admin.ModelAdmin):
    list_display = friendfindermatch.list_display
    fields = friendfindermatch.fields

