def ascending():
    vList=[23,20,18,24,14,9,456,1]
    print(vList)
    for ct in range(1,len(vList)):
        pos=ct
        val=vList[ct]

        while (pos>0 and vList[pos-1]>val):
            vList[pos]=vList[pos-1]
            pos=pos-1
            vList[pos]=val
    print(vList)


def descending():
    vList=[23,20,18,24,14,9,456,1]
    print(vList)
    for ct in range(1,len(vList)):
        pos=ct
        val=vList[ct]

        while (pos>0 and vList[pos-1]<val):
            vList[pos]=vList[pos-1]
            pos=pos-1
            vList[pos]=val

    print(vList)

ascending()
descending()
