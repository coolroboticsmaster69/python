
vList = []
for x in range(0,10):
    user_input = int(input("enter a number: "))
    vList.append(user_input)

def ascending():
    print("your list" + str(vList))
    for ct in range(1,len(vList)):
        pos=ct
        val=vList[ct]

        while (pos>0 and vList[pos-1]>val):
            vList[pos]=vList[pos-1]
            pos=pos-1
            vList[pos]=val
    print("ascending order" + str(vList))


def descending():
    print("your list" + str(vList))
    for ct in range(1,len(vList)):
        pos=ct
        val=vList[ct]

        while (pos>0 and vList[pos-1]<val):
            vList[pos]=vList[pos-1]
            pos=pos-1
            vList[pos]=val

    print("desending order" + str(vList))

ascending()
descending()
