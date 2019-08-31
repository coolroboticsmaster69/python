print ("enter input number : ")

input1 = int(input())

sum1 = 0
product = 1

for y in range(0,input1+1):
	sum1 = sum1 + y


for z in range(1,input1+1):
	product = product * z


print ("the product is " + str(product))


print ("the sum is " + str(sum1))

