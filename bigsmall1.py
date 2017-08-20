import sys
max1 = -sys.maxint
min1 = sys.maxint
for x in xrange(1,10+1):
	print ("please enter a number from: " + str(x))
	user_input = int(raw_input())

	if user_input < min1:
		min1 = user_input

	if user_input > max1:
		max1 = user_input	

print ("bigest number is " + str(max1))

print ("smallest number is " + str(min1))			
	