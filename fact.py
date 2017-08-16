def fact2(y):
    if y>1:
        return (y*fact2(y-1))
    return (1)

print(fact2(5))
