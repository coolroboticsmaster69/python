name=input("tell me your name ")
rev=""
for ct in range(len(name)-1,-1,-1):
    rev=rev+name[ct]
print(rev)
