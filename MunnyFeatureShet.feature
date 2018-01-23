# Created by benjamin at 29/12/2017
Feature: GET request based MunnyID session memory.
  Such that we can negate a full login system but also recognise individual users i have implemented session code.
  In src.views.sessionview you will see a redirect to http://127.0.0.1:8000/src but also a parsing of the last data bit
  in the GET request. This will save that bit to a cookie where the getter for said cookie is request.sessions['munnyid']

  Scenario: Example: http://127.0.0.1:8000/src/sessions/NougnaweiuAeorea
    http://127.0.0.1:8000/src/sessions/<Encrpyted UserID>
    Encrpytion is brought to you by models.user it uses state of the art cesar ciphering.
    eg cesarcipher("User.__str__, User.id)
    at the end of src/sessions/

Feature: Speakercountry, Fruitperson, user???
  I made the three distinctions which goes as follows:
  *User:
  *Fruitperson:
  *Speakercountry:

  Scenario:



  Feature: Groups and Choices for Users
    Categories: [Ad, Exec, SO, , Press, Delegate, ambassador, judge & advocate, judge]
    Virtually mutually exclusive. (Fuck thomas)

    First group (category dependent):
      Ad-staff:
        [Committee, Kitchen Staff...?] <- Mutually exclusive ignore the judge clauses

      Delegate or ambassador:
        " A Committee name(Inherit ad-staff's)"

      Judge & Advocate or Judge:
        "International Court of Justice"

      Press:
        "Positions"

      Exec:
        "A Position" <- Long list, mutually exclusive

      Student Officer(SO):
        [Committee(Inherit Ad-staff's)]

    Second group(category and first group dependent):
      Student Officer:
        [President, VP, Chair, VC]
        This concatenates with committee choices.

      Delegate, Ambassador, Judge/ & Advocate:
        "Country list"


    href="/accounts/facebook/login/?process=login"