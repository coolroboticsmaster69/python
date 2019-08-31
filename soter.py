list1 = []
sum1 = 0
n = int((10*11)/2)
print("""please enter a number from 1 to 10
            all numbers should be there
            1 number should be repeated""")

for x in range(0,11):
    user_input = int(input(""))
    list1.append(user_input)

for x2 in list1:
    sum1 = sum1 + x2

n2 = sum1 - n

print (str(n2) + " was repeated,,,,,,,,,Right ????????????")  