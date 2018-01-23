from sys import path

from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'src'
urlpatterns = [
    # Maps the empty url (index) to the index page
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^fruit/', views.fruit, name='fruit'),
    url(r'^fruitleader/', views.fruitleader, name='fruitleader'),
    url(r'^ticketview/', views.ticketview, name='ticketview'),
    url(r'^sessions/', views.sessionsview, name='sessions'),
    url(r'^missingloginpage/', views.missingloginpage, name="missingloginpage"),
    url(r'^friendfinder/', views.friendfinderview, name="friendfinderview"),


]