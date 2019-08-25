num_list = []	

for x in range(1,10+1):
	print ("please enter a number " + str(x))
	user_input = int(input())
	num_list.append(user_input)

num_list.sort()

print (num_list)

print ("the smallest number that you gave is " + str(num_list[0]))

print ("the bigest number that you gave is " + str(num_list[-1]))
	