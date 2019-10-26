
num1 = 0
num2 = 1
numofFibon = int(input("please enter a number: "))
print(f"{num1} + 0 = 0")
print(f"{num1} + 1 = 1")
for x in range(0, numofFibon-2):

    newNum = num1 + num2
    print(f"{num1} + {num2} = {newNum}")
    num1 = num2
    num2 = newNum

