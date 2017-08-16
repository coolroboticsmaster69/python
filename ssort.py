def descending():
    vList=[23,20,18,24,14,9,456,1]
    print(vList)
    for ct in  range(len(vList)-1,0,-1 ):
        minn=9999999999999
        minp=0
        for cc in range(0,ct+1):
            if vList[cc] < minn:
                minn=vList[cc]
                minp=cc
        vList[minp]=vList[ct]
        vList[ct]=minn
    print(vList)


def ascending():
    vList=[23,20,18,24,14,9,456,1]
    print(vList)
    for ct in  range(len(vList)-1,0,-1 ):
        maxn=0
        maxp=0
        for cc in range(0,ct+1):
            if vList[cc] > maxn:
                maxn=vList[cc]
                maxp=cc
        vList[maxp]=vList[ct]
        vList[ct]=maxn
    print(vList)

ascending()
descending()
