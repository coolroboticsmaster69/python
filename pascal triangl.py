rows = int(input("how many rows do u want in da pascal triangle ?"))
pascal = 1
numbersList = []
for r in range(1, rows+1):
    pasNum = " " * (rows-r)
    rowList = []
    for c in range(1, r+1):
        pascal = 1
        if c != 1 and c != r:
            lastnumberlist = numbersList[r - 2]
            pascal = lastnumberlist[c - 2] + lastnumberlist[c - 1]
        rowList.append(pascal)
        pasNum = pasNum + str(pascal) + " "
    numbersList.append(rowList)
    print(pasNum)