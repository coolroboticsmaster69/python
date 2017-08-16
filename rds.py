import random
rVari=random.randint(1,20)
while True:
    ug=int(input("guess a number between 1-20 "))
    if rVari==ug:
        print( "good job you found the number")
        break
    elif rVari<ug:
        print("too high try again")
    else:
        print("too low try again")
