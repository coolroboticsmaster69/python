def ascending():
    vList=[23,20,18,24,14,9,456,1]
    print(vList)
    for ct in range(len(vList)-1,-1,-1):
        for cc in range(0,ct):
            viv=vList[cc]
            if vList[cc]>vList[cc+1]:
                vList[cc]=vList[cc+1]
                vList[cc+1]=viv
    print(vList)

def descending():
    vList=[23,20,18,24,14,9,456,1]
    print(vList)
    for ct in range(len(vList)-1,-1,-1):
        for cc in range(0,ct):
            viv=vList[cc]
            if vList[cc]<vList[cc+1]:
                vList[cc]=vList[cc+1]
                vList[cc+1]=viv
    print(vList)

ascending()
descending()
