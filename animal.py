import random

random_num = random.randint(1,51) 
found = False
for x in xrange(0,10):
	user_input = int(raw_input("guess a number from 1 - 50:"))
	if random_num > user_input:
		print ("go high")
	elif random_num < user_input:
		print ("go low")
	else:
		print ("bull, your number is equal to random number")
		found = True
		break	
if not found:
	print ("you lose bad luck the random number was this " + str(random_num))		