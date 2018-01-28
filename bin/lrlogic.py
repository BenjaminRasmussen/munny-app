def isFinished():
    # Create two lists of id's and nummer's
    svarid, svarnum, sortsvar = [], [], list(svar.objects.all())
    for x in sortsvar:
        svarid.append(x.getKey())
        svarnum.append(x.getnummer())

    # Sort out the duplicates
    temp = defaultdict(list)
    for delvt, pin in zip(svarid, svarnum):
        # TODO given the revelations of bugs will the sentiment of this line also be buggy?
        if temp[Livredderaktion.objects.last()].__contains__(pin):
            # Duplicate detected!
            pass
        else:
            # TODO Fix that not every unique number is attatched but that every unique and ID relevant number is attatched!
            # ERROR RIGHT HERE BUDDY
            if svar.objects.get(nummer=pin, id=delvt).getlinkedKey() == Livredderaktion.objects.last():
                temp[Livredderaktion.objects.last()].append(pin)
        #print(temp)

    dowehaveaasailorwithaboatlicense = False
    for i in temp[Livredderaktion.objects.last()]:
        if Livredderperson.objects.get(nummer=i).getboatrequirementbool():
            dowehaveaasailorwithaboatlicense = True
        else:
            pass
    #hasmetrequirement

    # List of numbers responding to ID of last aktion     List of needed responders to ID of last aktion.
    if len(temp[Livredderaktion.objects.last()]) >= Livredderaktion.objects.last().getintstop() and dowehaveaasailorwithaboatlicense:
        Livredderaktion.objects.last().flipfinished()

    return len(temp[Livredderaktion.objects.last()]) >= Livredderaktion.objects.last().getintstop() and dowehaveaasailorwithaboatlicense
