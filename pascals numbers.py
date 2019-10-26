rows = int(input("how many rows do you want  in pascal traingle ?"))
cols = 1
numbersList = []

for r in range(1,rows+1):
    pasNum = (rows-r) * " "
    rowList = []
    newNum = 1
    for c in range(1, r+1):

        newNum = 1
        if c != 1 and c != r:

            lastdot = numbersList[r - 2]
            newNum = lastdot[c - 2] + lastdot[c - 1]
        rowList.append(newNum)
        pasNum = pasNum + str(newNum) + " "
    numbersList.append(rowList)
    print(pasNum)
# print(numbersList)

