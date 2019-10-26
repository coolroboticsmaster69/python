
y = 1
oldy = 0
numofFibon = int(input("please enter a number: "))

for x in range(0, numofFibon-2):

    y = oldy + y
    oldy = y
print(y)