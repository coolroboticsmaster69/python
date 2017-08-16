name=input("tell me your name ")
aList=[]

def fname(xyz):
    if xyz<len(name)-1:
        fname(xyz+1)
    aList.append(name[xyz])

fname(0)
reverce=""
for value in aList:
    reverce=reverce+value
print(reverce)
