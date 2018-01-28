from sys import path

from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'src'
urlpatterns = [
    # Maps the empty url (index) to the index page
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),

    # Content pages from nav bar
    url(r'^fruit/', views.fruitleader, name='fruit'),
    url(r'^fruitleader/', views.fruitleader, name='fruitleader'),
    url(r'^ticketview/', views.ticketview, name='ticketview'),
    url(r'^sessions/', views.sessionsview, name='sessions'),
    url(r'^missingloginpage/', views.missingloginpage, name="missingloginpage"),
    url(r'^friendfinder/', views.friendfinderview, name="friendfinderview"),
    url(r'^suc/', views.suc, name="suc"),

    # Legal pages
    url(r'^credits/', views.creditsview, name="credits"),
    url(r'^PrivacyPolicy/', views.PricavyPolicyview, name="PrivacyPolicy"),
    url(r'^TOS', views.TOSview, name="TOS"),

    # AJAX call urls
    url(r'^test/', views.testview, name="test"),
    url(r'^ajaxcall/', views.ajaxcallview, name="ajaxcall"),
    url(r'^friendfinderajaxcall/', views.friendfinderajaxcall, name="friendfinderajaxcall")


]