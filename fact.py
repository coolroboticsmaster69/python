user_input = int(input("enter a number: "))

def fact2(y):
    if y>1:
        return (y*fact2(y-1))
    return (1)

print(fact2(user_input))
